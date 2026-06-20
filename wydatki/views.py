from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Wydatek
from .forms import WydatekForm

def lista_wydatkow(request):
    wydatki = Wydatek.objects.all()
    suma_calkowita = wydatki.aggregate(Sum('kwota'))['kwota__sum'] or 0

    podsumowanie = (
        wydatki
        .values('kategoria')
        .annotate(suma=Sum('kwota'))
        .order_by('-suma')
    )

    slownik_kategorii = dict(Wydatek._meta.get_field('kategoria').choices)
    for pozycja in podsumowanie:
        pozycja['nazwa'] = slownik_kategorii.get(pozycja['kategoria'], pozycja['kategoria'])

    kontekst = {
        'wydatki': wydatki,
        'suma_calkowita': suma_calkowita,
        'podsumowanie': podsumowanie,
    }
    return render(request, 'wydatki/lista.html', kontekst)


def dodaj_wydatek(request):
    if request.method == 'POST':
        form = WydatekForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_wydatkow')
    else:
        form = WydatekForm()

    return render(request, 'wydatki/formularz.html', {
        'form': form,
        'tytul': 'Dodaj nowy wydatek',
    })


def edytuj_wydatek(request, pk):
    wydatek = get_object_or_404(Wydatek, pk=pk)

    if request.method == 'POST':
        form = WydatekForm(request.POST, instance=wydatek)
        if form.is_valid():
            form.save()
            return redirect('lista_wydatkow')
    else:
        form = WydatekForm(instance=wydatek)

    return render(request, 'wydatki/formularz.html', {
        'form': form,
        'tytul': 'Edytuj wydatek',
    })


def usun_wydatek(request, pk):
    wydatek = get_object_or_404(Wydatek, pk=pk)

    if request.method == 'POST':
        wydatek.delete()
        return redirect('lista_wydatkow')

    return render(request, 'wydatki/usun.html', {'wydatek': wydatek})
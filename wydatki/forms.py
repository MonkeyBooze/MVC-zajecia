from django import forms
from .models import Wydatek

class WydatekForm(forms.ModelForm):
    class Meta:
        model = Wydatek
        fields = ['kategoria', 'kwota', 'data', 'opis']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'kwota': forms.NumberInput(attrs={'step}': '0.01', 'min': '0'}),
            'opis': forms.TextInput(attrs={'placeholder': 'np. Zakupy w Biedronce'}),
        }
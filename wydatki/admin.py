from django.contrib import admin
from .models import Wydatek

@admin.register(Wydatek)
class WydatekAdmin(admin.ModelAdmin):
    # konfiguracja panelu admina, zeby ladnie wygladalo
    list_display = ('kategoria', 'kwota', 'data', 'opis')
    list_filter = ('kategoria', 'data')
    search_fields = ('opis',)
    ordering = ('-data',)
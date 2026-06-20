from django.db import models

KATEGORIE = [
    ('jedzenie', 'Jedzenie'),
    ('transport', 'Transport'),
    ('mieszkanie', 'Mieszkanie'),
    ('rozrywka', 'Rozrywka'),
    ('zdrowie', 'Zdrowie'),
    ('inne', 'Inne'),
]

class Wydatek(models.Model):
    kategoria = models.CharField(
        max_length=20,
        choices=KATEGORIE,
        verbose_name='Kategoria'
    )
    kwota = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Kwota (zł)'
    )
    data = models.DateField(verbose_name='Data')
    opis = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Opis (opcjonalnie)'
    )

    class Meta:
        ordering = ['-data', '-id']
        verbose_name = 'Wydatek'
        verbose_name_plural = 'Wydatki'

    def __str__(self):
        return f'{self.get_kategoria_display()} - {self.kwota} zł ({self.data})'


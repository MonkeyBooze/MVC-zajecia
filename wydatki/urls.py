from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_wydatkow, name='lista_wydatkow'),
    path('dodaj/', views.dodaj_wydatek, name='dodaj_wydatek'),
    path('edytuj/<int:pk>/', views.edytuj_wydatek, name='edytuj_wydatek'),
    path('usun/<int:pk>/', views.usun_wydatek, name='usun_wydatek'),
]
# MVC-zajecia
Prosta aplikacja webowa w Django pozwalająca na śledzenie domowych wydatków.
Projekt zrealizowany w architekturze MVC (w Django: MVC).


## Spis treści

1. [Funkcjonalności](#funkcjonalności)
2. [Wymagania](#wymagania)
3. [Instalacja i uruchomienie](#instalacja-i-uruchomienie)
4. [Struktura projektu](#struktura-projektu)
5. [Przykładowe dane](#przykładowe-dane)

## Funkcjonalności

- **Lista wydatków** — wyświetla wszystkie zapisane wydatki posortowane po dacie
- **Dodawanie wydatku** — formularz z polami: kategoria, kwota, data, opcjonalny opis
- **Edycja wydatku** — modyfikacja istniejącego wpisu
- **Usuwanie wydatku** — z potwierdzeniem
- **Podsumowanie** — łączna suma wydatków oraz suma w rozbiciu na kategorie
- **Kategorie predefiniowane** — jedzenie, transport, mieszkanie, rozrywka, zdrowie, inne
- **Panel administracyjny** — wbudowany panel Django pod adresem `/admin/`

## Wymagania

- Python 3.10+
- Django 4.2+

## Instalacja i uruchomienie

### 1. Sklonuj repozytorium

```bash
git clone 
cd wydatki_projekt
```

### 2. Utwórz i aktywuj wirtualne środowisko

```bash
python -m venv venv
source venv/Scripts/activate
```

### 3. Zainstaluj zależności

```bash
pip install -r requirements.txt
```

### 4. Wykonaj migracje bazy danych

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. (Opcjonalnie) Załaduj przykładowe dane

```bash
python manage.py loaddata przykladowe_dane.json
```

### 6. (Opcjonalnie) Utwórz konto administratora

```bash
python manage.py createsuperuser
```

### 7. Uruchom serwer

```bash
python manage.py runserver
```

Aplikacja dostępna pod adresem: http://127.0.0.1:8000/

## Struktura projektu

Projekt zbudowany jest w schemacie MVC (w Django nazywanym MVC):

- **Model** (`wydatki/models.py`) — klasa `Wydatek` z polami kategoria, kwota, data, opis
- **Widok / Kontroler** (`wydatki/views.py`) — funkcje obsługujące żądania HTTP
- **Szablony** (`wydatki/templates/wydatki/`) — pliki HTML wyświetlające dane
- **Formularz** (`wydatki/forms.py`) — formularz do dodawania i edycji wydatków
- **Routing** (`wydatki/urls.py`) — mapowanie adresów URL na widoki

## Przykładowe dane

Plik `przykladowe_dane.json` zawiera kilka przykładowych wydatków do załadowania komendą:

```bash
python manage.py loaddata przykladowe_dane.json```
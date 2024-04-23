# Ćwiczenie 6: Normalizacja i składowanie danych

## Cel: Pobranie i normalizacja danych kursów walut udostępnianych przez NBP

Dla następujących walut:

USD

CHF

EUR

GBP

JPY

Pobierz dane o średnich kursach walut z ostatnich 25 udostępnionych wycen.
Opis API znajdziesz pod adresem: `http://api.nbp.pl/`

Używając API możesz skorzystać z parametru: `?format=json`.

Dane możesz pobrać używając "tabeli A" (opisana w dokumentacji API) lub pytając bezpośrednio o daną walutę za pomocą jej kodu.

Dokonaj normalizacji i zaproponuj diagram ERD w oparciu o pobierane dane.

Pobrane dane zapisz do pliku JSON.


### Wersja dla chętnych (dodatkowe 20% oceny z aktywności):
Przygotuj schemat relacyjnej bazy danych, stwórz bazę i dodaj do rozwiązania kod źródłowy zapisujący pobrane wyniki do bazy danych.
Do rozwiązania dołącz dump bazy danych do pliku SQL.

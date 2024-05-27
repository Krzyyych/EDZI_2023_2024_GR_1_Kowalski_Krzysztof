# Projekt 2 
## Cel
Celem projektu jest rozbudowa rozwiązania powstałego w ramach `Projektu 1` o relacyjną bazę danych oraz dodanie źródła danych w postaci zewnętrznego API.

## Wymagania:
1. Opracowanie schematu oraz implementacja relacyjnej bazy danych przechowującej model danych wypracowany w ramach Projektu 1. Model powinien zawierać następujące obiekty:
    * Oferta (tabela faktu)
        * ID Oferty
        * ID Stanowiska
        * ID Firmy
        * ID Kategorii
        * ID Waluty
        * ID Źródła
        * Link
        * Umiejętności (array z ID)
        * Seniority
        * Wynagrodzenie MIN
        * Wynagrodzenie MAX

    * Firma (wymiar)
    * Stanowisko (wymiar)
    * Umiejętności (wymiar)
    * Waluta (wymiar)
    * Źródło (wymiar, może być tabelą manualną)
    * Kategoria (wymiar, może być tabelą manualną)


2. Stworzenie podsumowania każdej pobranej oferty pracy i zapisanie jej w tabeli: `Oferta` w osobnym polu `Podsumowanie`.

3. Pobranie dodatkowych informacji o adresie firmy wystawiającej ogłoszenie korzystając z `OpenStreetMap API`

4. Co ma się znalezc w repozytorium?
    * Pliki programu napisanego w pythonie
    * Dump SQL bazy danych

5. Termin oddania projektu: `28.05.2024`

6. Uwagi końcowe

    * Do wykonania projektu można użyć danych ściągniętych w ramach projektu 1
    * Dobre praktyki
        * Modularyzacja
        * Obsługa wyjątków

    * Obsługa OpenStreetMap API
    ```python
        import requests

        def get_location(company_name):
            # Base URL for Nominatim API
            base_url = "https://nominatim.openstreetmap.org/search"
            # Parameters for the search query
            params = {
                "q": company_name,
                "format": "json",
                "addressdetails": 1  # Include address details in the response
            }
            # Make the request to Nominatim API
            response = requests.get(base_url, params=params)
            data = response.json()

            # Check if any results were found
            if data:
                # Extract location information from the first result
                location = {
                    "display_name": data[0]["display_name"]
                }
                return location
            else:
                return None

        # Example usage
        company_name = "Google"
        location = get_location(company_name)
        if location:
            print(f"Location for {company_name}:")
            print(f"Address: {location['display_name']}")
        else:
            print(f"No location found for {company_name}.")


7. Ocenianie
    * 4.0: Stworzona baza danych zawierająca wszystkie z opisanych składowych
    * 4.5: Dodanie podsumowania do oferty pracy
    * 5.0: Dodanie informacji o adresie firmy zatrudniającej
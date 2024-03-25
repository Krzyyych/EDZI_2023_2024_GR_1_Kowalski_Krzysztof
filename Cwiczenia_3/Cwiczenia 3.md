# Ćwiczenie 3: Porównanie popularności tytułów pomiędzy dwoma filmowymi bazami danych 

## Cel:
Celem ćwiczenia jest napisanie Crawlera, który wykona następujące kroki:

1. Pobierze listę 100 najbardziej popularnych filmów według serwisu : `https://www.imdb.com/` wraz z ich oceną
2. Dla każdego filmu z listy, pobierze wynik procentowy z serwisu: `https://www.rottentomatoes.com`
3. Wynik końcowy zapisze w postaci pliku JSON  w formacie: `{"tytul_filmu": string, "ranking_imdb": int, "ocena_imdb": number, "ocena_rotten_tomatoes": int}`

* Należy dodać obsługę potencjalnych problemów z ekstrakcją danych lub dostępem do zasobu
* Dane pobrane z obu serwisów powinny współdzielić ten sam model danych
* Zgodność z plikiem `robots.txt` musi być sprawdzana
* Wynik końcowy w postaci pliku JSON proszę załączyć jako rozwiązanie wraz z kodem programu

Podpowiedź 1: Szukając filmów do porównania warto skorzystać z wbudowanej w serwis rottentomatoes.com funkcji szukania, a konkretniej sposobu w jaki budowany jest URL z szukaną frazą.

Podpowiedź 2: Jak wymusić język angielski podczas pobierania zawartości strony? - poprzez dodanie odpowiedniego headera

```
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Accept-Language': 'en-US,en;q=0.9'}

response = requests.get(url, headers=headers)
```
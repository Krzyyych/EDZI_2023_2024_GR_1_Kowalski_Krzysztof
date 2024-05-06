# Ćwiczenie 7: NLP i tworzenie podsumowania tekstu

## Cel: Pobranie tekstu artykułu z Wikipedii oraz utworzenie dla niego podsumowania.

Za pomocą Wikipedia API `https://www.mediawiki.org/wiki/API:Main_page/pl` pobierz tekst dowolnego artykułu angojęzycznego (użyj endpointa EN: https://en.wikipedia.org/w/api.php) a następnie utwórz jego podsumowanie za pomocą jednej z poniżej wymienionych bibliotek:

- https://pypi.org/project/sumy/
- https://pypi.org/project/bert-extractive-summarizer/
- https://pypi.org/project/gensim/


Tekst oryginalny zapisz w pliku wynikowym o nazwie `org.txt` a podsumowanie w pliku `outcome.txt`

Do pobrania tekstu artykułu, możesz użyć przykładowego kodu (kod pobiera tekst z dobrze znanej z CW1 strony : https://en.wikipedia.org/wiki/Web_scraping):

```python
import requests

def get_random_wikipedia_article_text():
    # Endpoint URL for the MediaWiki API
    endpoint = "https://en.wikipedia.org/w/api.php"

    article_params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "titles": "Web_scraping", #Here come the title you want to get
        "explaintext": True  # Return plain text instead of HTML
    }
    article_response = requests.get(endpoint, params=article_params)
    if article_response.status_code == 200:
        article_data = article_response.json()
        # Extract the text of the article
        article_text = next(iter(article_data["query"]["pages"].values()))["extract"]
        return article_text
    else:
        print("Failed to fetch article text")

# Example usage:
random_article_text = get_random_wikipedia_article_text()
print(random_article_text)

```

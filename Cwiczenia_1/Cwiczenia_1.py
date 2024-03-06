import requests
from bs4 import BeautifulSoup

def get_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # mw-parser-output to klasa HTML uzywana na platformie MediaWiki - jest glownym kontenerem dla tresci
    content = soup.find('div', class_='mw-parser-output').text
    return content

def process_text(text):
    text_new = ''.join(char for char in text if char.isalnum() or char.isspace())
    return text_new.lower()

def get_ranked_words(text):
    ranked_words = {}
    words = text.split()
    for word in words:
        if word in ranked_words:
            ranked_words[word] += 1
        else:
            ranked_words[word] = 1

    ranked_words = sorted(ranked_words.items(), key=lambda x: x[1], reverse=True)
    return ranked_words[:100]

def write_results(results, filename):
    with open(filename, 'w') as file:
        i = 1
        for words in results:
            file.write(f'{i};{words[0]};{words[1]}\n')
            i += 1

def main():
    url = 'https://en.wikipedia.org/wiki/Web_scraping'
    text = get_text(url)
    cleaned_text = process_text(text)
    final_words = get_ranked_words(cleaned_text)
    write_results(final_words, 'output.txt')

if __name__ == "__main__":
    main()
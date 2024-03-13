from bs4 import BeautifulSoup
import requests
import random

def get_a(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('a')

def get_href(a):
    links = []
    for l in a:
        href = l.get('href')
        if href and href.startswith('http'):
            links.append(href)
    return links

def jumps(links, first_link, n_jumps=100):
    for i in range(n_jumps):
        random_link = random.choice(links)
        print(f'W iteracji {i} startujac z {first_link} wylosowano: {random_link}')
        a = get_a(random_link)
        links = get_href(a)
        if len(links) == 0:
            links = get_href(get_a(first_link))
            print('Brak linkow na kolejnej stronie. Przechodzenie do kolejnej iteracji.')
            continue
        first_link = random_link

def main():
    first_link = 'https://www.onet.pl/'
    a = get_a(first_link)
    links = get_href(a)
    jumps(links, first_link)

if __name__ == "__main__":
    main()
from movies_ranking.scrapping_validation import is_scrapping_allowed
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

def imdb_top_100():
    base = "https://m.imdb.com/"
    url = "https://m.imdb.com/chart/top/?ref_=nv_mv_250"
    if not is_scrapping_allowed(base, url):
        print(f"Scrapping from {url} is not allowed.!")
        return None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Accept-Language': 'en-US,en;q=0.9'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return pd.DataFrame({'Title': get_movies(soup), 'Rating': get_ratings(soup)})
    else:
        print("Failed to retrieve IMDb top 100.")
        return None

def get_movies(bs):
    movies_header = bs.select('.cli-title h3.ipc-title__text')
    movies = [movie.text.strip() for movie in movies_header][:100]
    movies = [re.sub('[0-9]+. ', '', movie) for movie in movies]
    return movies

def get_ratings(bs):
    ratings_header = bs.select('.ipc-rating-star--imdb')
    ratings = [rating.text.strip() for rating in ratings_header][:100]
    ratings = [re.search(r'(\d+\.\d+)', rating).group(0) for rating in ratings]
    return ratings
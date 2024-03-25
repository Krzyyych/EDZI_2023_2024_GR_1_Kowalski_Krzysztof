from movies_ranking.scrapping_validation import is_scrapping_allowed
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests

def rotten_tomatoes(movie_title):
    base = "https://www.rottentomatoes.com/"
    url = f"https://www.rottentomatoes.com/search?search={movie_title.replace(' ', '+')}"
    if not is_scrapping_allowed(base, url):
        print(f"Scrapping from {url} is not allowed.!")
        return None
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3', 'Accept-Language': 'en-US,en;q=0.9'}
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        score = get_score(soup)
    else:
        print("Failed to retrived Rotten Tomatoes")
        return None

def get_score(bs):
    score_header = bs.select('.search__container search-page-media-row')
    scores = [score.get('tomatometerscore') for score in score_header]
    try:
        score = next((s for s in scores if s != ''), None)
        #print(score)
    except Exception as e:
        print(e)
        score = "Score not found"
    return score
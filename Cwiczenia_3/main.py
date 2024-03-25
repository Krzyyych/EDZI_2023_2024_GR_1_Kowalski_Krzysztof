from movies_ranking.scrapping_validation import is_scrapping_allowed
from movies_ranking.imdb import imdb_top_100
from movies_ranking.rotten_tomatoes import rotten_tomatoes
import pandas as pd

def main():
    imdb = imdb_top_100()
    m = s = r = []
    movies = imdb['Title']
    for movie in movies:
        score = rotten_tomatoes(movie)
        rating = imdb[imdb['Title'] == movie]['Rating'].iloc[0]
        m.append(movie)
        s.append(score)
        r.append(rating)
    df = pd.DataFrame({"tytul_filmu": movie, "ranking_imdb": list(range(0, 100)), "ocena_imdb": rating, "ocena_rotten_tomatoes": score})
    with open('Ranking_filmow.txt', 'w') as file:
        file.write(df.to_json(orient = 'records', lines = True))



if __name__ == '__main__':
    main()


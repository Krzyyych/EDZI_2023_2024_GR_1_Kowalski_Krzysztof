from api_imgw import api_imgw
import pandas as pd

def main():
    miasta_wojewodzkie = ["warszawa", "krakow", "lodz", "wroclaw", "poznan", "gdansk", "szczecin",
                          "lublin", "bialystok", "katowice", "torun", "kielce", "rzeszow", "gorzow", "opole", "olsztyn", "torun"]
    df_columns = ['miasto', 'data', 'temperatura', 'opady', 'cisnienie']
    df = pd.DataFrame(columns = df_columns)
    for miasto in miasta_wojewodzkie:
        dane = api_imgw.pobierz_dane_pogodowe_miasta(miasto)
        if dane:
            dict_to_df = {'miasto': dane['stacja'], 'data': dane['data_pomiaru'] + " " + dane['godzina_pomiaru'] + "H", 'temperatura': float(dane['temperatura']), 'opady': float(dane['suma_opadu']), 'cisnienie': float(dane['cisnienie'])}
            df = pd.concat([df, pd.DataFrame([dict_to_df])], ignore_index=True)
    api_imgw.print_weather(df)
    api_imgw.save_to_json(df, 'dane_pogodowe.json')

if __name__ == "__main__":
    main()


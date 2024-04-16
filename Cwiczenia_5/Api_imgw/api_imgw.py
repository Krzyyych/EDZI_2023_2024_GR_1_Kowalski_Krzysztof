import requests
import json
from statistics import mean
import pandas as pd
import numpy as np

def pobierz_dane_pogodowe_miasta(miasto):
    url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"
    response = requests.get(url)
    if response.status_code == 200:
        dane = response.json()
        return dane
    else:
        print(f"Błąd pobierania danych dla miasta: {miasto}")
        return None

def print_weather(df):
    print("-------------------------------------------------------------------")
    print("Data pomiaru:", df['data'][0])
    print("-------------------------------------------------------------------")
    print("TEMPERATURA")
    print("Średnia tempetatura:", round(np.mean(df['temperatura']), 2))
    print("Minimalna tempetatura:", np.min(df['temperatura']), 'wystąpiła w',
          df.loc[df['temperatura'] == np.min(df['temperatura']), 'miasto'].values[0])
    print("Maksymalna tempetatura:", np.max(df['temperatura']), 'wystąpiła w',
          df.loc[df['temperatura'] == np.max(df['temperatura']), 'miasto'].values[0])
    print("-------------------------------------------------------------------")
    print("CISNIENIE")
    print("Średnie ciśnienie:", round(np.mean(df['cisnienie']), 2))
    print("Minimalne ciśnienie:", np.min(df['cisnienie']), 'wystąpiło w',
          df.loc[df['cisnienie'] == np.min(df['cisnienie']), 'miasto'].values[0])
    print("Maksymalne ciśnienie:", np.max(df['cisnienie']), 'wystąpiło w',
          df.loc[df['cisnienie'] == np.max(df['cisnienie']), 'miasto'].values[0])
    print("-------------------------------------------------------------------")
    print("SUMA OPADOW")
    print("Średnia suma opadów:", round(np.mean(df['opady']), 2))
    print("Minimalna suma opadów:", np.min(df['opady']), 'wystąpiła w',
          df.loc[df['opady'] == np.min(df['opady']), 'miasto'].values[0])
    print("Maksymalna suma opadów:", np.max(df['opady']), 'wystąpiła w',
          df.loc[df['opady'] == np.max(df['opady']), 'miasto'].values[0])
    print("-------------------------------------------------------------------")

def save_to_json(df, path):
    data_to_save = {
        "Data pomiaru": df['data'][0],
        "TEMPERATURA": {
            "Średnia temperatura": round(np.mean(df['temperatura']), 2),
            "Minimalna temperatura": {
                "Wartość": np.min(df['temperatura']),
                "Miasto": df.loc[df['temperatura'] == np.min(df['temperatura']), 'miasto'].values[0]
            },
            "Maksymalna temperatura": {
                "Wartość": np.max(df['temperatura']),
                "Miasto": df.loc[df['temperatura'] == np.max(df['temperatura']), 'miasto'].values[0]
            }
        },
        "CISNIENIE": {
            "Średnie ciśnienie": round(np.mean(df['cisnienie']), 2),
            "Minimalne ciśnienie": {
                "Wartość": np.min(df['cisnienie']),
                "Miasto": df.loc[df['cisnienie'] == np.min(df['cisnienie']), 'miasto'].values[0]
            },
            "Maksymalne ciśnienie": {
                "Wartość": np.max(df['cisnienie']),
                "Miasto": df.loc[df['cisnienie'] == np.max(df['cisnienie']), 'miasto'].values[0]
            }
        },
        "SUMA OPADOW": {
            "Średnia suma opadów": round(np.mean(df['opady']), 2),
            "Minimalna suma opadów": {
                "Wartość": np.min(df['opady']),
                "Miasto": df.loc[df['opady'] == np.min(df['opady']), 'miasto'].values[0]
            },
            "Maksymalna suma opadów": {
                "Wartość": np.max(df['opady']),
                "Miasto": df.loc[df['opady'] == np.max(df['opady']), 'miasto'].values[0]
            }
        }
    }

    with open(path, 'w') as file:
        json.dump(data_to_save, file, indent=4)

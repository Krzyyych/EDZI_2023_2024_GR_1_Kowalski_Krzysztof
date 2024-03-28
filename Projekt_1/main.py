import json
import pandas as pd
from collections import Counter
from oferty.pracuj import it_pracuj
from oferty.justjoin import justjoin_it
from oferty.analiza import categorize_position
from oferty.analiza import add_seniority_to_category
from oferty.analiza import calculate_average_salary
from oferty.analiza import plot_skills_frequency
from oferty.analiza import plot_position_category_statistics
import matplotlib.pyplot as plt

def main():
    try:
        pracuj = it_pracuj()
        if pracuj is not None:
            print("Successfully fetched job links from it.pracuj.pl")
        else:
            print("Failed to fetch job links from it.pracuj.pl")

        justjoin = justjoin_it()
        if justjoin is not None:
            print("Successfully fetched job links from justjoin.it")
        else:
            print("Failed to fetch job links from justjoin.it")

        if pracuj is not None and justjoin is not None:
            all_jobs = pracuj + justjoin
            for idx, job in enumerate(all_jobs, start=1):
                job["Id"] = idx

            with open('jobs_data.json', 'w', encoding='utf-8') as f:
                json.dump(all_jobs, f, indent=4, ensure_ascii=False)

        df = pd.read_json('jobs_data.json', encoding='utf-8')
        df.set_index('Id', inplace=True)

        df['Seniority'] = df['Seniority'].replace(" Senior", "Senior")
        df['Seniority'] = df['Seniority'].replace(" Junior", "Junior")
        df = df[df['Seniority'] != 'hybrid work']  # Remove 1 incorrect row
        df = df[~df['Min salary'].str.contains(',', na=False)]

        all_skills = [skill for sublist in df['Skills'] for skill in sublist]
        skills_counter = Counter(all_skills)
        top_10_skills = skills_counter.most_common(10)
        skills_df = pd.DataFrame(top_10_skills, columns=['Skill', 'Częstotliwość'])

        df['Kategoria Pozycji'] = df['Pozycja'].apply(categorize_position)
        df['Kategoria Pozycji'] = df.apply(add_seniority_to_category, axis=1)
        df['Average salary'] = df.apply(calculate_average_salary, axis=1)
        positions_info = df.groupby('Kategoria Pozycji').agg({
            'Min salary': ['min'],
            'Max salary': ['max'],
            'Average salary': ['mean']
        }).reset_index()
        positions_info.columns = positions_info.columns.droplevel()
        positions_info = positions_info.rename(columns={'': "Kategoria Pozycji"})
        positions_info['mean'] = round(positions_info['mean'])

        category_counts = df['Kategoria Pozycji'].value_counts()
        category_counts = category_counts.to_frame().reset_index()
        category_counts.columns = ['Kategoria Pozycji', 'Liczba Wystąpień']
        wynikowa = pd.merge(category_counts, positions_info, on='Kategoria Pozycji')
        wynikowa = wynikowa[wynikowa['Kategoria Pozycji'] != "Other"]


        plot_skills_frequency(skills_df)
        plt.show()
        plot_position_category_statistics(wynikowa)
        plt.show()

        skills_json = skills_df.to_json(orient='records')
        statystyki_pozycji_json = wynikowa.to_json(orient='records')

        with open("skills.json", "w") as json_file:
            json_file.write(skills_json)

        with open("statystyki_pozycji.json", "w") as json_file:
            json_file.write(statystyki_pozycji_json)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
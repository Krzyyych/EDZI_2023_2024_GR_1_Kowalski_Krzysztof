import pandas as pd
import matplotlib.pyplot as plt
import re

def categorize_position(position):
    if re.search(r'\b(Mid Data Engineer|Data Engineer)\b', position, re.IGNORECASE):
        return "Data Engineer"
    elif re.search(r'\b(Mid Data Analyst|Data Analyst)\b', position, re.IGNORECASE):
        return "Data Analyst"
    elif re.search(r'\b(Mid Data Scientist|Data Scientist)\b', position, re.IGNORECASE):
        return "Data Scientist"
    elif re.search(r'\b(Mid Data Architect|Data Architect)\b', position, re.IGNORECASE):
        return "Data Architect"
    else:
        return "Other"

def add_seniority_to_category(row):
    if row['Seniority'] in ['Junior', 'Senior'] and row['Kategoria Pozycji'] != 'Other':
        return f"{row['Seniority']} {row['Kategoria Pozycji']}"
    else:
        return row['Kategoria Pozycji']

def calculate_average_salary(row):
    min_salary = row['Min salary']
    max_salary = row['Max salary']
    if pd.notnull(min_salary) and pd.notnull(max_salary):
        return (max_salary + min_salary) / 2
    else:
        return None

def plot_skills_frequency(skills_df):
    skills_df.plot(kind = 'bar', x = 'Skill', y = 'Częstotliwość', color = 'skyblue', figsize = (10, 6))
    plt.title('10 najbardziej pożądanych umiejętności')
    plt.xlabel('Skill')
    plt.ylabel('Częstotlwiość wystąpień')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.grid(True)


def plot_position_category_statistics(wynikowa):
    bar_width = 0.25
    index = wynikowa.index
    plt.figure(figsize = (14, 10))
    plt.bar(index, wynikowa['min'], bar_width, label='Min')
    plt.bar(index + bar_width, wynikowa['max'], bar_width, label='Max')
    plt.bar(index + (2 * bar_width), wynikowa['mean'], bar_width, label='Mean')

    plt.xlabel('Kategoria Pozycji')
    plt.ylabel('Liczba Wystąpień')
    plt.title('Statystyki liczby wystąpień dla każdej kategorii pozycji')
    plt.xticks(index + bar_width, wynikowa['Kategoria Pozycji'], rotation=15)
    plt.legend()
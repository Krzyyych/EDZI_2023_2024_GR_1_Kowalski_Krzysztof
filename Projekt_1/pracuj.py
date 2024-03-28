import requests
from bs4 import BeautifulSoup
import re

def it_pracuj():
    try:
        links_jump = []
        url_page = "https://it.pracuj.pl/praca/krakow;wp?rd=0&et=17%2C4%2C18&sal=1&its=big-data-science"
        response_page = requests.get(url_page)
        if response_page.status_code != 200:
            print("Failed to retrieve main page from it.pracuj.pl")
            return None

        soup_page = BeautifulSoup(response_page.text, 'html.parser')
        pages = soup_page.select('.listing_n1mxvncp.listing_n1mxvncp')
        if pages:
            pages_number = 2
        else:
            pages_number = 1

        for i in range(1, pages_number + 1):
            url = "https://it.pracuj.pl/praca/krakow;wp?rd=0&et=17%2C4%2C18&sal=1&its=big-data-science&pn=" + str(i)
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                pracuj_header = soup.select('.c1fljezf .core_n194fgoq')
                links = [link['href'] for link in pracuj_header if 'href' in link.attrs]
                pattern = re.compile(r'^https://www.pracuj.pl/praca/')
                filtered_links = [link for link in links if pattern.match(link)]
                links_jump.extend(filtered_links)
            else:
                print(f"Failed to retrieve page {i} from it.pracuj.pl")
                continue

        links_jump = list(set(links_jump))
        return jump_to_link_pracuj(links_jump)  # Assuming jump_to_link_pracuj is defined elsewhere
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def jump_to_link_pracuj(links):
    try:
        jobs_data = []
        source = "it.pracuj.pl"
        category = "BigData/Data Science"
        currency = "PLN"
        for link in links:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                position = soup.select('.offer-viewzJYJpV .offer-viewkHIhn3')[0].contents[0]

                company = soup.select('.offer-viewwtdXJ4')[0].contents[0]

                kind = soup.select('.offer-viewSGW6Yi')[0].contents[0]
                mth_or_h = re.search(r'\b(hr|mth|mies|godz)\.$', kind).group(1)
                gross_or_net = re.search(r'\b(brutto|gross|netto|net)\b', kind).group(1)

                min_salary = soup.select('.offer-viewZGJhIB')
                if min_salary:
                    min_salary = min_salary[0].contents[0]
                    min_salary = re.sub(r'[^\d,.]', '', min_salary)
                    min_salary = min_salary.replace(',', '.')
                    min_salary = min_salary.split('.')[0]
                    min_salary = int(min_salary)
                    max_salary = soup.select('.offer-viewYo2KTr')[0].contents[0]
                    max_salary = re.sub(r'[^\d,.]', '', max_salary)
                    max_salary = max_salary.replace(',', '.')
                    max_salary = max_salary.split('.')[0]
                    max_salary = float(max_salary)
                    if mth_or_h in ['godz', 'hr']:
                        if gross_or_net in ['netto', 'net']:
                            min_salary *= 168 * 1.23
                            max_salary *= 168 * 1.23
                        else:
                            min_salary *= 168
                            max_salary *= 168
                    else:
                        if gross_or_net in ['netto', 'net']:
                            min_salary *= 1.23
                            max_salary *= 1.23
                    min_salary = round(min_salary)
                    max_salary = round(max_salary)
                else:
                    min_salary_element = soup.select('.offer-viewYo2KTr')
                    if min_salary_element:
                        min_salary = min_salary_element[0].contents[0]
                    else:
                        min_salary = None
                        max_salary = None
                    max_salary = None

                seniority_str = soup.select('.offer-viewXo2dpV')[2].contents[0]
                if ',' in seniority_str:
                    if 'ekspert' in seniority_str:
                        seniority = seniority_str.split(',')[0]
                    else:
                        seniority = seniority_str.split(',')[1]
                else:
                    seniority = seniority_str

                seniority = seniority.replace("starszy specjalista (Senior)", "Senior").replace(
                    "specjalista (Mid / Regular)", "Mid").replace("junior specialist (Junior)", "Junior")
                seniority = seniority.replace('senior specialist (Senior)', "Senior").replace(" senior specialist (Senior)",
                                                                                              "Senior").replace(
                    " mÅ\x82odszy specjalista (Junior)", "Junior").replace('specialist (Mid / Regular)', 'Mid')
                skills_all = soup.select(".offer-viewfjH4z3:first-of-type .offer-viewU0gxPf")
                skills = [skill.text.strip() for skill in skills_all]
                job_data = {
                    "Źródło": source,
                    "Link": link,
                    "Pozycja": position,
                    "Firma": company,
                    "Min salary": min_salary,
                    "Max salary": max_salary,
                    "Currency": currency,
                    "Skills": skills,
                    "Category": category,
                    "Seniority": seniority
                }
                jobs_data.append(job_data)
            else:
                print(f"Nie można pobrać strony: {link}")
        return jobs_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


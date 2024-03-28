import requests
from bs4 import BeautifulSoup

def justjoin_it():
    try:
        url = "https://justjoin.it/krakow/data/experience-level_junior.mid.senior/with-salary_yes"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            justjoin_header = soup.select('.css-4lqp8g ')
            links = [link['href'] for link in justjoin_header if 'href' in link.attrs]
            links = ["https://justjoin.it" + link for link in links]
            return jump_to_link_justjoin(links)
        else:
            print("Failed to retrieve data from justjoin.it")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def jump_to_link_justjoin(links):
    try:
        jobs_data = []
        source = "justjoin.it"
        category = "Data"
        for link in links:
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                position = soup.select('.css-wx6bq4')[0].contents[-1].text

                company = soup.select('.css-u51ts9>*:not(:last-of-type)')[0].contents[1]

                seniority = soup.select('.css-15wyzmd')[1].contents[0]
                seniority = seniority.replace(" Senior", "Senior")

                min_salary = float(soup.select('.css-1pavfqb')[0].contents[0].text.replace(" ", ""))
                max_salary = float(soup.select('.css-1pavfqb')[0].contents[2].text.replace(" ", ""))
                currency = soup.select('.css-1pavfqb')[0].contents[5]

                skills_all = soup.select('.css-x1xnx3')
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
                print(f"Failed to retrieve data from: {link}")
        return jobs_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
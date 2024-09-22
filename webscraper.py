from bs4 import BeautifulSoup
import requests

# User can ask for their skill
skills = input("Give me a skill you are looking for in a job: ")
time = int(input("How many days ago must the job post have been made? Enter number: "))
html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords={skills}&txtLocation=').text

soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
for job in jobs:
        
        # Posted dates
        published_date = job.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date:
              days_posted = 3
        elif 'today' in published_date:
              days_posted = 0
        else:
            try:
                days_posted = int(''.join(filter(str.isdigit, published_date)))
            except ValueError:
                days_posted = 100
        
        if days_posted <= time:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text
            more_info = job.header.h2.a['href']

            print(f'{published_date}')
            print(f"Company Name: {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f'More Info: {more_info}')

            print('')

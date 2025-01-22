from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(response.content, 'lxml')
jobs = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
for job in jobs:
    publishedDate = job.find('span', class_='sim-posted').span.text
    if 'few' in publishedDate:

        companyName = job.find('h3', class_ = 'joblist-comp-name').text.strip()

        skillsSection = job.find('div', class_ = 'more-skills-sections')

        skills = ' '.join(span.text.strip() for span in skillsSection.find_all('span'))if skillsSection else "N/A"
        
        print(f"company Name : {companyName}")
        print(f"Required Skills : {skills}")
        
        print('')






 
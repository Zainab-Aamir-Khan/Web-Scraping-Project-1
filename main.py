from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
soup = BeautifulSoup(response.content, 'lxml')
job = soup.find('li', class_ ="clearfix job-bx wht-shd-bx")
companyName = job.find('h2', class_ = 'heading-trun').text.replace(' ', '')
print(companyName)
skills = job.find('li', class_ = 'job-description__').text
print(skills)


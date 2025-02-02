from bs4 import BeautifulSoup
import requests
import time

print("enter unfamiliar skills!!!")
unfamiliarSkills = input(">")
print(f'filtering out!!! : {unfamiliarSkills}')

def findJobs():
    response = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=')
    soup = BeautifulSoup(response.content, 'lxml')
    jobs = soup.find_all('li', class_ ="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        publishedDate = job.find('span', class_='sim-posted').span.text
        if 'few' in publishedDate:
            companyName = job.find('h3', class_ = 'joblist-comp-name').text.strip()
            skillsSection = job.find('div', class_ = 'more-skills-sections')
            skills = ' '.join(span.text.strip() for span in skillsSection.find_all('span'))if skillsSection else "N/A"
            moreInfo = job.header.h2.a('href')
            if unfamiliarSkills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:

                    f.write(f"company Name! : {companyName} \n")
                    f.write(f"Required Skills! : {skills} \n")
                    f.write(f"More Information! : {moreInfo} \n")
                print(f'file saved: {index}')    

if __name__ == '__main__':
    while True:
        findJobs() 
        timeWait = 10
        print(f"Waiting {timeWait} minutes...")
        time.sleep(timeWait * 600)



 
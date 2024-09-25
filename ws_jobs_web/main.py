# import requests
# from bs4 import BeautifulSoup
# import csv
# from itertools import zip_longest

# #fetch url
# result=requests.get(r"https://www.indeed.com/jobs?q=python&l=Remote&ts=1727179231724&from=searchOnHP&rq=1&rsIdx=0&fromage=last&vjk=52108bd7282a4c2d")

# #save page contents/markup
# src=result.content

# # transformin byte to markup lang
# soup=BeautifulSoup(src,'lxml')



# #find the elements containing info we searching for
# job_title=soup.find_all('h2',{'class':'jobTitle css-198pbd eu4oa1w0',})
# print(job_title)

#_________________________________ ubove code does not work due to the website is dynamicly content release so using Selenium library work best
#____________________________________________#____________________________________________#____________________________________________#_______


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from fake_useragent import UserAgent
# import time
# import random

# # Path to your chromedriver executable
# chrome_driver_path = "C:/chromedriver-win64/chromedriver.exe"

# # Set up the WebDriver service
# service = Service(chrome_driver_path)

# # Create a UserAgent instance
# ua = UserAgent()
# user_agent = ua.random

# # Set up Chrome options
# options = Options()
# options.add_argument(f"user-agent={user_agent}")  # Apply the random user agent
# options.add_argument("user-data-dir=C:/Users/**/AppData/Local/Google/Chrome/User Data")
# options.add_argument("profile-directory=Profile 2")  # Change to your profile directory if needed

# # Create the driver
# driver = webdriver.Chrome(service=service, options=options)

# # Open the Indeed page
# url = "https://www.indeed.com/jobs?q=python&l=Remote"
# driver.get(url)

# # Implicit wait
# driver.implicitly_wait(20)

# try:
#     # Introduce random delays
#     time.sleep(random.uniform(2, 5))

#     # Wait for the job titles to be present on the page
#     job_titles = WebDriverWait(driver, 20).until(
#         EC.presence_of_all_elements_located((By.XPATH, "//h2[contains(@class, 'jobTitle css-198pbd eu4oa1w0')]"))
#     )

#     # Print job titles
#     for job_title in job_titles:
#         print(job_title.text)

# except Exception as e:
#     print(f"An error occurred: {e}")
#     print(driver.page_source)  # Print page source for debugging if needed

# finally:
#     # Close the WebDriver
#     driver.quit()




#____________________________________________________________________________________________________________________------------

# from requests_html import HTMLSession

# # Create an HTML session
# session = HTMLSession()

# # Open the Indeed page
# url = "https://www.indeed.com/jobs?q=python&l=Remote"
# response = session.get(url)

# # Render the JavaScript
# response.html.render(sleep=5)  # Adjust sleep time as needed

# # Find job titles
# job_titles = response.html.xpath("//h2[contains(@class, 'jobTitle css-198pbd eu4oa1w0')]/span/text()")

# # Print job titles
# for job_title in job_titles:
#     print(job_title)


#___________________________________________________________________________________________________________________________________________


# import requests
# from bs4 import BeautifulSoup
# import csv
# from itertools import zip_longest

# #fetch url
# result=requests.get("https://wuzzuf.net/search/jobs/?q=python&a=hpb")

# #save page content/markup
# src= result.content

# #create soup object to parse content
# soup=BeautifulSoup(src,'lxml')


# job_title=[]
# company_name=[]
# location_name=[]
# skills=[]

# #links for every job to get deep description about it
# links=[]


# # job info
# job_titles=soup.find_all('h2',{'class':'css-m604qf'})

# company_names=soup.find_all('a',{'class':'css-17s97q8'})

# location_names=soup.find_all('span',{'class':'css-5wys0k'})

# job_skills=soup.find_all('div',{'class':'css-y4udm8'})


# # iterate over list to extract needed info into othter list
# for i in range(len(job_titles)):
#     job_title.append(job_titles[i].text)
#     links.append(job_titles[i].find('a').attrs['href'])
#     company_name.append(company_names[i].text)
#     location_name.append(location_names[i].text)
#     skills.append(job_skills[i].text)
    
    
# # iterate on every links to get more descriptions for each job
# for link in links:
#     result=requests.get(link)
#     src=result.content
#     soup=BeautifulSoup(src,'lxml')
#     salaries=soup.find_all('div',{'class':'css-rcl8e5'})
#     print(salaries)
    


# file_list=[job_title,company_name,location_name,skills,links]

# exported=zip_longest(*file_list)

# with open(f"C:/Users/NIPEAL/OneDrive/Desktop/projectss/py_project_githubs/web_scraping/ws_jobs_web/jobstest.csv" , 'w',newline='',encoding='utf-8') as f:
#     wr=csv.writer(f)
#     wr.writerow(['job title', 'company name', 'locaton','skills','links'])
#     wr.writerows(
#          exported
#     )
    
#_____________________________________________________________________________________________________________________________________________________________________
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
 
# Creating a webdriver instance
chrome_driver_path = "C:/chromedriver-win64/chromedriver.exe"
service = Service(chrome_driver_path)

# This instance will be used to log into LinkedIn
driver = webdriver.Chrome(service=service)

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
 
# waiting for the page to load
time.sleep(5)
 
# entering username 
username = driver.find_element(By.ID, "username")
 
# In case of an error, try changing the element
# tag used here.
 
# Enter Your Email Address
username.send_keys("")  
 
# entering password
pword = driver.find_element(By.ID, "password")
# In case of an error, try changing the element 
# tag used here.
 
# Enter Your Password
pword.send_keys("")        
 
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"
 
driver.get(profile_url)  
driver

#dd 
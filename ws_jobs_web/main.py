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
"""
The By class in selenium.webdriver.common.by is used to locate elements within a web page. It provides a set of attributes that 
represent different strategies for locating elements. Here are some common attributes you can use with By:
    By.ID: Locate an element by its ID attribute.
    By.NAME: Locate an element by its name attribute.
    By.XPATH: Locate an element using an XPath expression.
    By.CSS_SELECTOR: Locate an element using a CSS selector.
    By.CLASS_NAME: Locate an element by its class name.
    By.TAG_NAME: Locate an element by its tag name.
    By.LINK_TEXT: Locate a link element by its visible text.
    By.PARTIAL_LINK_TEXT: Locate a link element by a partial match of its visible text.
"""
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
#______________________________________________________________________________________________1_____________   
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


#______________________________________________________________________________________________2_____________   
# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"
 
driver.get(profile_url)  
driver



#______________________________________________________________________________________________3_____________   
#  Now, we need to scroll to the bottom. Here is the code to do that:
start = time.time()
 
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll 
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
 
    # we will stop the script for 3 seconds so that 
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
 
    end = time.time()
 
    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break
    
    
#______________________________________________________________________________________________4_____________   
# Extracting Data from the Profile
# To extract data, firstly, store the source code of the web page in a variable. Then, use this source 
# code to create a Beautiful Soup object.


src = driver.page_source
 
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')


# Extracting the HTML of the complete introduction box
# that contains the name, company name, and the location
intro = soup.find('div', {'class': 'mt2 relative'})

name=intro.find('h1').get_text().strip()
works_at_loc = intro.find("div", {'class': 'text-body-medium'}).text.strip()
location_loc = intro.find_all("span", {'class': 'text-body-small inline t-black--light break-words'})[0].get_text().strip()
print("Name -->", name,
      "\nWorks At -->", works_at_loc,
      "\nLocation -->", location_loc)


# Getting the HTML of the Experience section in the profile
experience = soup.find_all("section", {"class": "artdeco-card pv-profile-card break-words mt2"})[1].find('ul')


# exp=soup.find("section", {"class": "artdeco-card pv-profile-card break-words mt2"}).find_all('ul')
# print(experience==exp[0])  #True

#first exp find to simplify
print(experience.find('div').find_all('span')[0].text.strip())
print(experience.find('div').find_all('span')[3].text.strip())
print(experience.find('div').find_all('span')[6].text.strip())


for ex in experience.find_all('div',{'class':"OdisdwCWMtMIJFjwkkjUxJQnurvqaXgQaOX vsAATKtKqqHJBCXrRWgKkmUUPJwuUuo NwliYhHDezFmMFZUqschmUCeDCUsgXzjQoo"}):
    print(ex.find_all('span')[0].text.strip())
    print(ex.find_all('span')[3].text.strip())
    print(ex.find_all('span')[5].text.strip())
    print("__________________")
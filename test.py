import time
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
soup = BeautifulSoup(driver.page_source, features="lxml")

url = 'https://www.python.org/downloads/'
driver.get(url)

pythons = []

divs = soup.find_all('span', class_='release-number')
for div in divs:
    pythons.append(div.text)    

print(pythons)

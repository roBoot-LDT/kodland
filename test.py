import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://author.today/reader/230092'
driver.get(url)
soup = BeautifulSoup(driver.page_source, features="lxml")
divs = soup.find('div', id='text-container')
for p in divs:
    print(p.text)
time.sleep(2)

import time
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

project_id = input('Пожалуйста введите project ID: ')
driver.get(f"https://hub.kodland.org/ru/project/{project_id}")
time.sleep(10)

soup = BeautifulSoup(driver.page_source, features="lxml")
project_name = soup.find('h3', class_='post-title pt-3 pr-3').text
info_tags = soup.find_all('span', class_='stat__number')

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

for i in range(1, 100):
  url = f'https://nekdo.ru/page/{i}/'
  driver.get(url)
  soup = BeautifulSoup(driver.page_source, features="lxml")
  divs = soup.find('div', class_='text')
  for div in divs:
      print(div.text)
  time.sleep(2)

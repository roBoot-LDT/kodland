import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(f"https://nekdo.ru/page/2/")
soup = BeautifulSoup(driver.page_source)
for id in range(426780, 426820):
  anec = soup.find('div', class_='text', id=id)
  print(anec)
  

      

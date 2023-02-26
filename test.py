import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2")
soup = BeautifulSoup(driver.page_source, features="lxml")
print(soup.prettify())
table = soup.find('table', class_='wikitable').find('tbody')

print(table.prettify())
for link in table.find_all('a'):
  print(link.get("title"))       

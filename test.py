import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


for page in range(101):
  driver.get(f"https://nekdo.ru/page/{page}")
  time.sleep(1)

      

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://www.python.org")
soup = BeautifulSoup(driver.page_source, features="lxml")
print(soup.prettify())

for link in soup.find_all('a'):
    url = link.get('href')
    if 'https' in url or 'http' in url:
        driver.get(url)
    else:
        driver.get("https://www.python.org"+url)
    time.sleep(3)

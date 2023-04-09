import time
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import defaultdict
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

search_engine = int(input("Выберите поиск по:\n1. Википедия\n2. Энциклопедия\n(1/2) "))
if search_engine == 1:
    user_request = input("Что вы хотите найти в Википедии? ")
    url = f'https://ru.wikipedia.org/wiki/{user_request}'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    answer = soup.find('p')
    print(answer.text)
elif search_engine == 2:
    pass
else:
    print("Выбери корректную цифру!!!")

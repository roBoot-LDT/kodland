import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

id = input("Введите id проекта: ")
driver.get(f'https://hub.kodland.org/ru/projects/{id}')
time.sleep(10)

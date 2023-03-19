from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:5000/")

login = driver.find_element(By.NAME, "login")
password = driver.find_element(By.NAME, "password")
button = driver.find_element(By.TAG_NAME, "button")

print(login, password, button)

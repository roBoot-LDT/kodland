import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/auth/")

login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')
button = driver.find_element(By.TAG_NAME, 'button')

login.send_keys("mnemkov7")
password.send_keys("*******")
button.click()
time.sleep(2)

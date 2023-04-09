import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/auth/")

time.sleep(1)
login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')
 
button = driver.find_element(By.TAG_NAME, 'button')

login.send_keys('fmuhin5')
time.sleep(1)
password.send_keys('EwfyIgtC0v')
time.sleep(1)
button.click()
time.sleep(2)

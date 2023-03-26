import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:5000/")

login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME,'password')
button = driver.find_element(By.TAG_NAME, 'button')

login.send_keys('admin')
time.sleep(1)
password.send_keys('admin')
time.sleep(1)
button.click()
time.sleep(1)
contacts = driver.find_element(By.NAME, 'contacts')
contacts.click()
time.sleep(3)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:5000/contacts")
time.sleep(1)

login = driver.find_element(By.NAME, 'login')
login.send_keys('admin')

password = driver.find_element(By.NAME, "password")
password.send_keys("admin")

button = driver.find_element(By.TAG_NAME, 'button')
button.click()

time.sleep(4)

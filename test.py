import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/auth/")

login = driver.find_element(By.NAME, 'login')
password = driver.find_element(By.NAME, 'password')
button = driver.find_element(By.TAG_NAME, 'button')

time.sleep(1)
login.send_keys("mnemkov7")
time.sleep(1)
password.send_keys("******")
time.sleep(1)
button.click()
time.sleep(2)
driver.get('https://platform.kodland.org/en/task_56514/')
time.sleep(1)
button1 = driver.find_element(By.ID, 'sub-button')
time.sleep(1)
button1.click()
time.sleep(1)
button2 = driver.find_element(By.ID, "submit_task_button")
time.sleep(1)
button2.click()
time.sleep(3)

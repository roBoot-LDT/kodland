from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://platform.kodland.org/")
urls = ["https://platform.kodland.org/",
         "http://www.python.org",
           "https://binarypiano.com/",
             "http://corndog.io/",
               "https://longdogechallenge.com/",
                 "https://checkbox.toys/scale/",
                 "https://onesquareminesweeper.com/",
                   "https://puginarug.com/",
                     "https://paint.toys/calligram/"]
for i in urls:
    driver.get(i)
    time.sleep(2)

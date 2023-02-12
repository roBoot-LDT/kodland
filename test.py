from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

number = 0
driver = webdriver.Chrome(ChromeDriverManager().install())
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
    page = driver.page_source
    file_ = open(f'page{number}.html', 'w', encoding='utf-8')
    file_.write(page)
    file_.close()
    number += 1

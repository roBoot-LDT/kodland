import time
from selenium import webdriver
from bs4 import BeautifulSoup
from collections import defaultdict
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
req = input("Что вы хотите найти? ")
driver.get(f'https://ru.wikipedia.org/wiki/{req}')
soup = BeautifulSoup(driver.page_source, features='lxml')
time.sleep(2)
def find_only_main(tag):
    return tag.has_attr('p') and tag.has_attr('b')

data =  soup.find_all('p')
for answer in data:
    print(find_only_main(answer))
# for answer in data:
    
#     print(type(answer))
#     print(answer.text+"\n")

# anecs = defaultdict(list)
# for i in range(1, 2):
#     url = f'https://nekdo.ru/page/{i}/'
#     driver.get(url)
#     soup = BeautifulSoup(driver.page_source, features="lxml")
#     divs_text = soup.find_all('div', class_='text')
#     divs_meta = soup.find_all('div', class_='cat')
#     for div_text, div_meta in zip(divs_text, divs_meta):
#         a_tags = div_meta.find_all('a')
#         for a_tag in a_tags:
#             anecs[a_tag.text].append(div_text.text)
#     time.sleep(2)

# with open('anecs.pickle', 'wb') as f:
#     pickle.dump(anecs, f)

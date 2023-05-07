import requests
from bs4 import BeautifulSoup
import time
while True:
    search_term = input("Введите термин для поиска:")

    url = f"https://ru.wikipedia.org/wiki/{search_term}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Страница для запроса '{search_term}' не найдена.")
    else:
        soup = BeautifulSoup(response.text, "html.parser")

        title = soup.find("h1", {"class": "firstHeading"}).text
        paragraphs = soup.find_all("p")

        for data in paragraphs:
            if search_term in data.text:
                print(data.text)
                break
        # first_paragraph = None
        # if len(paragraphs) > 0:
        #     first_paragraph = paragraphs[0].text

        # print("Заголовок страницы:")
        # for letter in title:
        #     print(letter, end="", flush=True)
        #     time.sleep(0.02)
        # print("\nКраткая справка:")
        # if first_paragraph is not None:
        #     for letter in first_paragraph:
        #         print(letter, end="", flush=True)
        #         time.sleep(0.02)
        # else:
        #     print("Абзацы на странице не найдены.")

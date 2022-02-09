import requests
import json
from bs4 import BeautifulSoup

url = "https://astrakhan.kupiprodai.ru/realty/astrahan_kvartiry/param804"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

adv_info = soup.find_all('div', {'class': 'list_info'})

parsed_data = []

for adv in adv_info:
    parsed_data.append ({
        'title': adv.find('a', {'class': 'list_title'}).text,
        'link': adv.find('a', {'class': 'list_title'}).get('href'),
         "Параметры": adv.find('p', {'class': 'list_text'}).text,
    })
with open('gg/parsed_data.json', 'w') as f:

    json.dump(
        parsed_data[0:5:1],
        f,
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )
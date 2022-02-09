import json

with open('MailSearch/card.json') as f:
    datas = json.load(f)
    name = input("Ввведите имя: ").strip()
    for dicts in datas:
        if name in dicts["name"]:
            print("email:", dicts["email"])
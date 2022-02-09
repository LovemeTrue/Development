import os.path
import json

name = input("Ваше имя: ").strip()

while True:
    age = input("Ваш возраст: ")
    if (age.isnumeric()):
        age = int(age)
        break
    else:
        print ('Ошибка! Введите целое число')


company = input("Компания, в которой вы работаете: ").strip()

pets_name = input("Имя домашнего животного: ").strip()

while True:
    phone_number = input("Ваш номер: ").strip()
    if (phone_number.isnumeric()):
        phone_number = int(phone_number)
        break
    else:
        print ('Ошибка! Введите целое число')

while True:
    filename = input('Введите имя файла: ')
    if (os.path.isfile(filename)):
        break
    print ('Такого файла не существует')


data = {
    "name": name,
    "age": age,
    "company": company,
    "pets_name": pets_name,
    "phone_number": phone_number
}
with open("Asker/db.json", "r") as file:
    try: 
        dataZ = json.load(file)
    except:
        dataZ = []

with open("Asker/db.json","w") as file:
    dataZ.append(data)
    json.dump(dataZ, file)

path = 'Asker/db.json'

with open('Asker/db.json') as f:
    datas = json.load(f)
    for dicts in datas:
        print("Имя:", dicts["name"])
        print("Возраст:", dicts["age"])
        print("Компания:", dicts["company"])
        print("Имя животного:", dicts["pets_name"])
        print("Номер телефона:", dicts["phone_number"])
        print("\n")
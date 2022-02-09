import requests


def getJsonURL(url):
    reqJson = requests.get(url)
    return reqJson.json()

def sDate():
    id = input("Введите дату начала в формате дд-мм-гггг: ").strip()
    return id

def eDate():
    id = input("Введите дату конца в формате дд-мм-гггг: ").strip()
    return id

def firstVal():
    while True:
        id = input("Введите 'Код' валюты 1: ").strip()
        if(id.isnumeric()):
            id = int(id)
            break
        else:
            print('Ошибка! Введите существующее целое число!')
    return id

def secondVal():
    while True:
        id = input("Введите 'Код' валюты 2: ").strip()
        if(id.isnumeric()):
            id = int(id)
            break
        else:
            print('Ошибка! Введите существующее целое число!')
    return id

def user_input():
    while True:
        id = input("Введите 'ID' пользователя: ").strip()
        if(id.isnumeric()):
            id = int(id)
            break
        else:
            print('Ошибка! Введите существующее целое число!')
    return id

def search_input():
    id = input("Введите 'текст поиска': ").strip()
    return id

def serach_id_post():
    while True:
        id = input("Введите 'ID' поста: ").strip()
        if(id.isnumeric()):
            id = int(id)
            break
        else:
            print('Ошибка! Введите существующее целое число!')
    return id
from liberty import *
import requests
import xmltodict
url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='


start_date = sDate().split('/')
end_date = eDate().split('/')

# first_val = firstVal()
# second_val = secondVal()


url_start = url + start_date[0] + "/" + start_date[1] + "/" + start_date[2]
# url_end = url + end_date[0] + "/" + end_date[1] + "/" + end_date[2]

# print(url_start)
# print(url_end)


xmldata = requests.get(url_start)
# xmldata = requests.get(url_end)

xmlDict = xmltodict.parse(xmldata.content)

calendar_days = [
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31
]


if int(start_date[2]) % 4 == 0 or int(start_date[2]) % 100 == 0 and int(start_date[2]) % 400 == 0:
    calendar_days[1] = 28
else:
    calendar_days[1] = 29


print(calendar_days[1])

xmldata = False

for valute in xmlDict['ValCurs']['Valute']:
    print (xmlDict['ValCurs']['@Date'])
    print (valute['CharCode'])
    print (valute['Value'])
   

# for valute in xmlDict['ValCurs']['Valute']:

#     print (valute['CharCode'])
#     print (valute['Value'])

#В общем, задача.
# Скрипт при запуске сначала спрашивает дату начала, потом дату конца
# Потом спрашивает первую валюту, а потом вторую
# И выводит подневно курсы этих двух валют

# То есть, запускаешь скрипт.
# Он говорит, "введите дату начала в формате дд-мм-гггг"
# Потом "введите дату конца в формате дд-мм-гггг"
# Потом "Введите код валюты 1 (USD, EUR и т.п.)"
# Потом "Введите код валюты 2 (USD, EUR и т.п.)"

# И потом выводит данные в таком формате:

# 12-11-2009
# USD - 30
# EUR - 45

# 13-11-2009
# USD - 31
# EUR - 42

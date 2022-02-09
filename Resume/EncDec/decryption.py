from myLib import *

text = input("Введите имя файла")

while True:
   shiftnum = input('Введите смещение: ')
   if (shiftnum.isnumeric()):
      shiftnum = int(shiftnum)
      break
   else:
      print('Ошибка! Введите целое число')

while True:
   choose = str(input("Введите 1 для кодирования и 2 для декодирования: "))
   if (choose == '1' or choose == '2'):
      choose = int(choose)
      break
   else:
      print('Ошибка! Введите 1, либо 2')

print ("Все данные введены")

new = ''

for letter in text:
   if (choose == 1):
      new = new + encrypt_symbol(letter,shiftnum)
   else:
      new = new + decrypt_symbol(letter,shiftnum)

print(new)
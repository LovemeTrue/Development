from EncDec.myLib import encrypt_symbol
from caesarlib import *
import os.path

while True:
    filename = input('Введите имя файла: ')
    if (os.path.isfile(filename)):
        break
    print ('Такого файла не существует')

while True:
    shiftnum = input('Введите смещение: ')
    if (shiftnum.isnumeric()):
        shiftnum = int(shiftnum)
        break
    else:
        print ('Ошибка! Введите целое число')

while True:
    choose = str(input('Введите 1 для кодирования и 2 для декодирования: '))
    if (choose == '1' or choose == '2'):
        choose = int(choose)
        break
    else:
        print ('Ошибка! Введите либо 1, либо 2')

new = ''

filehandler = open(filename,'r')
filelines = filehandler.readlines()

for line in filelines:
    for letter in line.rstrip("\n"):
        if (choose == 1):
            new = new + encrypt_symbol(letter,shiftnum)
        else:
            new = new + decrypt_symbol(letter,shiftnum)
    new = new + "\n"

filehandler.close()

resfilename = input('Введите имя файла результата: ')
resfile = open(resfilename,'w')
resfile.write(new)
resfile.close()
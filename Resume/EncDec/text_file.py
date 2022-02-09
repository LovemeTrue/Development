from myLib import *

text = "rttrt"

encrypt = 2
decrypt = 0

i = 0

new = ""
decr = ""

while i < len(text):
   new = new + encrypt_symbol(text[i],encrypt)
   decr = decr + decrypt_symbol(text[i],decrypt)
   i = i + 1

print(new)


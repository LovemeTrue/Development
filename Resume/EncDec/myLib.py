def encrypt_symbol(symbol,enc_num):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   newsymbol_index = alphabet.index(symbol) + enc_num
   if newsymbol_index >= len(alphabet):
      newsymbol_index = newsymbol_index - len(alphabet)
   return (alphabet[newsymbol_index])

def decrypt_symbol(symbol,enc_num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newsymbol_index = alphabet.index(symbol) - enc_num
    return (alphabet[newsymbol_index])
    
class coderClass:
  
    def __init__(self, symbol):

        self.symbol = symbol

    def __str__(self):

        return self.symbol

    def set(self, symbol):
        
        self.symbol = symbol

    def __sub__(self, enc_num):

        return(self.__add__(-enc_num))


    def __add__(self, enc_num):
        
        self.enc_num = enc_num
        
        new_enc = ""
        
        for letter in self.symbol:
    
            new_enc = new_enc + self.encrypt_symbol(letter, self.enc_num)
    
        return new_enc
    
    def encrypt_symbol(self, letter, enc_num):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        alphabet = alphabet + alphabet.upper()
        alphabet = alphabet + '0123456789'
        if (letter not in alphabet):
            return (letter)
        newsymbol_index = alphabet.index(letter) + enc_num
        if newsymbol_index >= len(alphabet):
            newsymbol_index = newsymbol_index - len(alphabet)
        return (alphabet[newsymbol_index])

class child(coderClass):
    
    def __mul__(self, enc_num):
        
        return (self.__add__(enc_num) and self.__sub__(-enc_num))

    def __truediv__(self, enc_num):

        return self.__mul__(-enc_num)
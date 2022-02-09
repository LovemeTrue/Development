class stringFormating:
    
    string = ""
    
    def __init__(self, string):
        
        self.string = string

    def reverse(self):
        
        self.string = self.string[::-1]
        
        return self.string

    def strrts(self):

        self.string = self.string + self.string[::-1]

        return self.string

    def set(self, string):
        
        self.string = string
        
    def get(self):

        self.string

        return self.string
    
class strClass(stringFormating):

    def watafaq(self,string):

        return string.join(self.string)

    def setBrackets(self, string):
    
       super().set(str(string).join('""'))
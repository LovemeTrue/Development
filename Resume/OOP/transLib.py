from googletrans import Translator

class transClass:

    def __init__(self):

        self.translator = Translator()
        
    def setString(self, string):

        self.string = string

    def get(self):

        self.string

        return self.string

    def setLang(self, lang):

        lang = self.translator.translate(self.string, src = lang)

        return lang
 
    def getTranslate(self, lang):
        
        self.string = self.translator.translate(self.string, dest = lang)

        return self.string


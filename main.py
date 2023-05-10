from deep_translator import GoogleTranslator
class ldt:
    def __init__(self):
        self.GoodWords = ""
        self.WordsToMix = ""
        self.langList = ['en','af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'co', 'hr', 'cs', 'da', 'dv', 'doi',  'nl', 'eo', 'et', 'ee', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja', 'en']
    def getWords(self):
        goodwords = input("what do you want me to jumble up?")
        self.GoodWords = goodwords
        self.WordsToMix = goodwords
        
    def langLoop(self):
        for jumble in range(1,len(self.langList)):
            self.WordsToMix = GoogleTranslator(source=self.langList[jumble - 1], target=self.langList[jumble]).translate(self.WordsToMix)
            

trans =  ldt() 
trans.getWords()
trans.langLoop()
print(trans.WordsToMix)

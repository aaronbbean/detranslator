from deep_translator import GoogleTranslator
from random import choice , shuffle
#
# Decide is I want to read and write to a file.
#
class ldt:
    def __init__(self):
        self.GoodWords = ""
        self.WordsToMix = ""
        self.pastpick = "en"
        self.presentpick = ""
        # Decide if I want to add this option
        self.loopnumber = ""
        #I need to get all the languages
        self.langList = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'co', 'hr', 'cs', 'da', 'dv', 'doi',  'nl', 'eo', 'et', 'ee', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja']
    def getWords(self):
        goodwords = input("what do you want me to jumble up?")
        self.GoodWords = goodwords
        self.WordsToMix = goodwords
        shuffle(self.langList)
    def langLoop(self):

        for jumble in range(0,len(self.langList)):
            if jumble == 15 or jumble == 30:
                
                print(GoogleTranslator(source=self.pastpick, target="en").translate(self.WordsToMix))
            
            self.presentpick = choice(self.langList)
            if self.presentpick == self.pastpick:
                self.presentpick = choice(self.langList)
            self.WordsToMix = GoogleTranslator(source=self.pastpick, target=self.langList[self.presentpick]).translate(self.WordsToMix)    
            self.pastpick = self.presentpick
        print(GoogleTranslator(source=self.pastpick, target="en").translate(self.WordsToMix))

trans =  ldt() 
trans.getWords()
trans.langLoop()
print(trans.WordsToMix)         



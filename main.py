from deep_translator import GoogleTranslator
from random import choice , shuffle

class ldt:
    def __init__(self):
        self.GoodWords = ""
        self.WordsToMix = ""
        self.pastpick = "en"
        self.presentpick = ""
        self.langList = ['af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bho', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'co', 'hr', 'cs', 'da', 'dv', 'doi',  'nl', 'eo', 'et', 'ee', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja']

    def getWords(self):
        shuffle(self.langList)
        goodwords = open("Words.txt","r")
        SplittingWords = goodwords.read()
        
        self.GoodWords = SplittingWords.split()
        goodwords.close()
        self.WordsToMix = self.GoodWords
    def langLoop(self):
        writingWords = open("Words.txt","a")
        for jumble in range(0,2):

            if jumble == 15 or jumble == 30:
                writingWords.write("\n")
                writingWords.write(GoogleTranslator(source=self.pastpick, target="en").translate(self.WordsToMix))
            """This needs to be modified. The translator needs more letters."""
            try:
                for getRidOfSingles in range(len(self.WordsToMix)):
                
                    if len(self.WordsToMix[getRidOfSingles]) == 1:
                        print("Good")
                        
                        if getRidOfSingles + 1 > len(self.WordsToMix):
                            self.WordsToMix[getRidOfSingles] += " " + "".join(self.WordsToMix[getRidOfSingles : getRidOfSingles]) 
                            del self.WordsToMix[getRidOfSingles + 1]
                print(self.WordsToMix)
            except:print("")
            self.presentpick = choice(self.langList)
            
            if self.presentpick == self.pastpick:
                self.presentpick = choice(self.langList)

            for singleWord in range(len(self.GoodWords)):

                self.WordsToMix[singleWord] = GoogleTranslator(source=self.pastpick, target=self.presentpick).translate(self.WordsToMix[singleWord])    
            self.pastpick = self.presentpick
            print(self.WordsToMix)
        writingWords.write("\n")    
        writingWords.write(GoogleTranslator(source=self.pastpick, target="en").translate(self.WordsToMix))
        writingWords.close()
    def test(self):
        pass
        


trans =  ldt() 

trans.getWords()
trans.langLoop()

print(trans.WordsToMix)         



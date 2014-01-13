from nltk import word_tokenize

class AlliterationFinder:

    def __init__(self):
        self.f = ""
        self.counter = 0

    #Path is inputted from AIPController
    #Returns alliteration counter
        
    def sendFile(self, path):
        self.f = open(path)
        for line in self.f:
            try: self.counter += self.get_all_allits(line)
            except: continue
        c = self.counter
        self.counter = 0
        return c

    #Returns the length of an array which contains all
    #instances of alliteration

    def get_all_allits(self, line):
        allits = []
        try:
            first_word = word_tokenize(line)[0].lower()
        except:
            pass
        for w in word_tokenize(line)[1:]:
            if w[0].lower() == first_word[0]:
                allits.append([first_word, w])
            else:
                first_word = w.lower()
        return len(allits)



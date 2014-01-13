from nltk import word_tokenize

class AnaphoraFinder:

    def __init__(self):
        self.f = ""
        self.counter = 0
        self.first_word = ""
        self.b = False

    #Path is inputted from AIPController
    #Returns anaphora counter
        
    def sendFile(self, path):
        self.f = open(path)
        for line in self.f:
            try:
                if self.b:
                    self.counter += self.get_all_anaphora(line)
                else:
                    try:
                        self.first_word = word_tokenize(line)[0].lower()
                    except:
                        continue
                    self.counter += self.get_all_anaphora(line)
            except:
                continue
        c = self.counter
        self.counter = 0
        return c

    #Returns the length of an array which contains all
    #instances of anaphora

    def get_all_anaphora(self, line):
        ana = []
        for w in word_tokenize(line)[1:]:
            try:
                new_word = self.get_next_word(line, w).lower()
            except:
                pass
            if w.find('.') != -1 or w.find('!') != -1 or w.find('?') != -1:
                if new_word == self.first_word:
                    ana.append([self.first_word, new_word])
                    self.first_word = new_word
                elif new_word == False:
                    self.b = True
                else:
                    self.first_word = new_word
        return len(ana)

    #Gets the next word after the period for
    #anaphora comparison. If end-of-line and
    #would be IndexError, return False

    def get_next_word(self, line, target):
        tokens = word_tokenize(line)[1:]
        for w in range(len(tokens)):
            if tokens[w] == target:
                try:
                    return tokens[w+1].lower()
                except:
                    return False
            

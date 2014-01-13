from nltk import word_tokenize

class EpistropheFinder:

    def __init__(self):
        self.f = ""
        self.counter = 0
        self.last_word = ""

    #Path is inputted from AIPController
    #Returns epistrophe counter
        
    def sendFile(self, path):
        self.f = open(path)
        for line in self.f:
            try:
                self.counter += self.get_all_epistrophe(line)
            except:
                continue
        c = self.counter
        self.counter = 0
        return c

    #Returns the length of an array which contains all
    #instances of epistrophe

    def get_all_epistrophe(self, line):
        epi = []
        for w in word_tokenize(line):
            w = w.lower()
            if w == '.' or w == '?' or w == '!':
                prev_word = self.get_prev_word(line, w).lower()
                test = (prev_word != False)
                if test:
                    if self.last_word == prev_word:
                        epi.append([self.last_word, prev_word])
                        self.last_word = prev_word
                    elif self.last_word == "":
                        self.last_word = prev_word
                    else:
                        self.last_word = prev_word
            elif w.find('.') != -1 or w.find('!') != -1 or w.find('?') != -1:
                w = w.replace('.', '')
                w = w.replace('?', '')
                w = w.replace('!', '')
                if self.last_word == w:
                    epi.append([self.last_word, w])
                    self.last_word = w
                elif self.last_word == "":
                    self.last_word = w
                else:
                    self.last_word = w

        return len(epi)

    #Gets the previous word before the period for
    #epistrophe comparison. If end-of-line and
    #would be IndexError, return False

    def get_prev_word(self, line, target):
        tokens = word_tokenize(line)
        for w in range(len(tokens)):
            if tokens[w] == target:
                try:
                    return tokens[w-1]
                except:
                    return False
            


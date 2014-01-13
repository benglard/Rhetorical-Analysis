from DashFinder import DashFinder
from SemiFinder import SemiFinder
from AlliterationFinder import AlliterationFinder
from AnaphoraFinder import AnaphoraFinder
from EpistropheFinder import EpistropheFinder
from ParallelismFinder import ParallelismFinder
import time, subprocess, os

class Summarizer():

    def __init__(self, input_text, num_lines=None):

        self.text = input_text
        self.num_lines = num_lines

        self.counters = []
        self.finders = []
        self.probs = []
        self.weights = [.05, .05, .1, .2, .2, .4]
        self.weighted = []
        self.results = {}
        self.ranked = []

        self.dF = DashFinder()
        self.sF = SemiFinder()
        self.alF = AlliterationFinder()
        self.anF = AnaphoraFinder()
        self.eF = EpistropheFinder()
        self.pF = ParallelismFinder()

        self.finders.append(self.dF)
        self.finders.append(self.sF)
        self.finders.append(self.alF)
        self.finders.append(self.anF)
        self.finders.append(self.eF)
        self.finders.append(self.pF)

        self.folder = str(int(time.time()))
    	subprocess.call('mkdir ' + self.folder, shell=True)
    	self.path = "INPUT/A/PATH"

        self.lineCounter = 1

    def summarize(self):
        pos = 0
        self.text = self.text.replace('\n', '')

        while self.text != "":
            if self.text.find('.') != -1:
                pos = self.text.find('.')
                self.__find_strategies(self.text[:pos], pos+1)
            elif self.text.find('?') != -1:
                pos = self.text.find('?')
                self.__find_strategies(self.text[:pos], pos+1)
            elif self.text.find('!') != -1:
                pos = self.text.find('!')
                self.__find_strategies(self.text[:pos], pos+1)
            else:
                self.__find_strategies(self.text, len(self.text))

        self.__rank()

        subprocess.call('rm -rf ' + self.folder, shell=True)

        for sent, score in self.ranked[:self.num_lines]:
                print sent + "\n" #+ ' ' + str(score)

        return self.ranked[:self.num_lines]

    def __find_strategies(self, sentence, text_pos):
    	filename = str(self.lineCounter) + ".dat"
    	path = os.path.join(self.path, filename)

    	f = open(path, "w+")
        f.write(sentence)
        f.close()

        for finder in self.finders:
            self.counters.append(finder.sendFile( path ))

        self.text = self.text[text_pos:]

        total = float(sum(self.counters))
        if total != 0:
            self.probs.append(self.counters[0]/total)
            self.probs.append(self.counters[1]/total)
            self.probs.append(self.counters[2]/total)
            self.probs.append(self.counters[3]/total)
            self.probs.append(self.counters[4]/total)
            self.probs.append(self.counters[5]/total)

            for p,w in zip(self.probs, self.weights):
                self.weighted.append(p*w)

            score = sum(self.weighted)*sum(self.counters)/6
            self.results[sentence] = score

        self.probs = []
        self.weighted = []
        self.counters = []
        self.lineCounter += 1

    def __rank(self):
        while len(self.ranked) != len(self.results):
            sent = max(self.results, key=self.results.get)
            score = self.results[sent]
            self.ranked.append([sent, score])
            self.results[sent] = 0

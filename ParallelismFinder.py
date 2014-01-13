from nltk import *
from nltk.corpus import brown

class ParallelismFinder:

    def __init__(self):
        self.f = ""
        self.counter = 0
        self.para = [] #array to hold instances of parallelism

        self.tokenizer = RegexpTokenizer('\w+') #remove punctuation which could mess up finding parallelism
        #Train tagger with subset of Brown News Corpus
        brown_news_tagged = brown.tagged_sents(categories='news')
        brown_train = brown_news_tagged
        self.tagger = UnigramTagger(brown_train) #Unigram Tagger based on Brown corpus

    #Path is inputted from AIPController
    #Returns parallelism counter

    def sendFile(self, path):
        self.f = open(path)
        for line in self.f:
            try:
                self.get_all_parallelism(line)
            except:
                continue
        c = self.counter
        self.counter = 0
        self.para = [] #re-initialize to empty array
        return c

    #Returns the parallelism counter

    def get_all_parallelism(self, line):
        sent = self.tokenizer.tokenize(line)
        tags = self.tagger.tag(sent)
        self.get_phrase_parallelism(tags, 1)
        self.get_phrase_parallelism(tags, 2) #Pairs of words
        self.get_phrase_parallelism(tags, 3) #Triplets of words
        self.get_phrase_parallelism(tags, 4) #Group of 4 words

    #Get parallelism between n_para # of words
    #Ex: the a
    #Ex: the bird, the word
    #Ex2: I came, I saw, I conquered
    #Ex: Of the people, by the people, for the people
    #Ex: the people are good, the people are bad

    def get_phrase_parallelism(self, tags, n_para):
        tagged1, tagged2 = [], []
        words1, words2 = [], []
        for n in range(0, len(tags)-n_para, n_para):
            try:
                tag_subset = tags[n:n+n_para]
                tag = self.get_tags(tag_subset)
                tagged1.append([tag])
                tag_subset = tags[n+n_para:n+(2*n_para)]
                tag = self.get_tags(tag_subset)
                tagged2.append([tag])
                word_subset = tags[n:n+n_para]
                words1 = self.get_words(word_subset)
                word_subset = tags[n+n_para:n+(2*n_para)]
                words2 = self.get_words(word_subset)
                if tagged1 == tagged2:
                    self.para.append([words1, words2])
                    self.counter += 1
                tagged1, tagged2 = [], []
                words1, words2 = [], []
            except:
                continue
    
    #Get tags of phrases for comparison
            
    def get_tags(self, tag_sub):
        ret = []
        for t in tag_sub:
            ret.append(t[1])
        return ret
    
    #Get words of phrases for entrance into instance array

    def get_words(self, word_sub):
        ret = []
        for t in word_sub:
            ret.append(t[0])
        return ret


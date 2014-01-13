class SemiFinder:

    def __init__(self):
        self.f = ""
        self.counter = 0

    #Path is inputted from AIPController
    #Returns semicolon counter

    def sendFile(self, path):
        self.f = open(path)
        for line in self.f:
            try:
                self.counter += self.get_all_semis(line)
            except:
                continue
        c = self.counter
        self.counter = 0
        return c

    #Gets next occurence of a semicolon
    #Retuns True/False value, position of semicolon

    def get_next_target(self, page):
        pos_semi = page.find(';')
        if pos_semi == -1: 
            return False, 0
        return True, pos_semi+1

    #Returns the length of an array which contains all
    #instances of semicolons

    def get_all_semis(self, page):
        semis = []
        while True:
            value, c = self.get_next_target(page)
            if value:
                semis.append(c)
                page = page[c:]
            else:
                break
        return len(semis)


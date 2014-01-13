class DashFinder:

    def __init__(self):
        self.f = ""
        self.counter = 0

    #Path is inputted from AIPController
    #Returns dash counter
        
    def sendFile(self, path):
        self.f = open(path)
        for line in self.f:
            try:
                self.counter += self.get_all_dashes(line)
            except:
                continue
        c = self.counter
        self.counter = 0
        return c

    #Gets next occurence of a dash
    #Retuns True/False value, position of dash,
    #not hyphens!
    
    def get_next_target(self, page):
        pos_dash = page.find(' - ')
        pos_dash2 = page.find(' -- ')
        pos_dash3 = page.find('--')
        if pos_dash == -1 and pos_dash2 == -1 and pos_dash3 == -1: 
            return False, 0
        return True, max([pos_dash, pos_dash2, pos_dash3])+1

    #Returns the length of an array which contains all
    #instances of dashes

    def get_all_dashes(self, page):
        dashes = []
        while True:
            value, c = self.get_next_target(page)
            if value:
                dashes.append(c)
                page = page[c:]
            else:
                break
        return len(dashes)


class FileParser(object):
    source = None
    def __init__(self,input = None):
        #here we set all the global variables that we need
        self.n = 0
        self.m = 0
        if input:
            self.source = open(input,"r")
    def init(self):
        self.n,self.m = self.source.readline().split(' ')
        self.n = int(self.n)
        self.m = int(self.m)
    def optimise(self):
        #herer we will implement our optimisation process
        pass
    def get_information(self):
        pass

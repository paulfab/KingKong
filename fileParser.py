class FileParser(object):
    source = None
    def __init__(self,input = None):
        #here we set all the global variables that we need
        self.row = 0
        self.column = 0
        self.drone = 0
        self.turn = 0
        self.max = 0
        if input:
            self.source = open(input,"r")
    def init(self):
        self.row,self.column,self.drone,self.turn,self.max = self.source.readline().split(' ')
    def optimise(self):
        #herer we will implement our optimisation process
        pass
    def get_information(self):
        pass

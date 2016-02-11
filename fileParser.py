class FileParser(object):
    source = None
    def __init__(self,input = None):
        #here we set all the global variables that we need
        self.row = 0
        self.column = 0
        self.drone = 0
        self.turn = 0
        self.max = 0
        self.product_types = 0
        self.products = {}
        self.orders = []
        self.warehouses = []
        if input:
            self.source = open(input,"r")
    def init(self):
        self.row,self.column,self.drone,self.turn,self.max = map(int, self.source.readline().split(' '))
        self.map = [[0 for x in range(self.row)] for x in range(self.column)]
        self.product_types = int(self.source.readline())
        weit = map(int,self.source.readline().split(' '))
        for i in weit:
            j = 0
            self.products[j] = Product(j,i)
            j = j+1
        self.warehouse_number = int(self.source.readline())
        for i in range(1,self.warehouse_number+1):
            ware = WareHouse()
            ware.x, ware.y = map(int,self.source.readline().split(' '))
            store = map(int,self.source.readline().split(' '))
            for i in range(1,self.product_types):
                ware.set_store(i,store[i-1])
            self.warehouses.append(ware)
        self.order_number = int(self.source.readline())
        for i in range(1,self.order_number+1):
            order = Order()
            order.x,order.y = map(int, self.source.readline().split(' '))
            order.quantity = int(self.source.readline())
            order.product_type = map(int,self.source.readline().split(' '))
            self.orders.append(order)
    def optimise(self):
        #herer we will implement our optimisation process
        pass
    def get_information(self):
        pass
class Drone(object):
    def __init__(self,id,payload):
        self.id = id
        self.payload = payload
        self.charge = None
        self.mouvement = []
    def rapport(self,source):
        #with this will give the last rapport
        pass
class Product(object):
    def __init__(self,type_= None,weigh= None):
        self.type_ = int(type_)
        self.weigh = weigh
class Order(object):
    def __init__(self,x= None,y= None,quantity= None):
        self.x = x
        self.y = y
        self.quantity = quantity
        self.product_type = []
class WareHouse(object):
    def __init__(self,x = None,y = None):
        self.x = x
        self.y = y
        self.store = {}
    def set_store(self,product,quantity):
        self.store[product]=[product,quantity]

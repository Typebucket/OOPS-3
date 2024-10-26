class computer:
    def __init__(self):
        self.__price = 5000
    
    def printvalue(self):
        print("The price of my computer is", self.__price)
    
    def setprice(self, price):
        self.__price = price

obj = computer()
obj.printvalue()
obj.__price = 1000
obj.printvalue()
obj.setprice(1005)
obj.printvalue()
class student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __method(self):
        print("Im inside the private method", self.__name , self.age)
    
    def normmethod(self):
        self.__method()
        print("Im in a normal method", self.__name , self.age)
    
obj = student("Kwesi", 13)
obj.normmethod()
print(obj.__name)

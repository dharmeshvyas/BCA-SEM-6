class Base:
    def __init__(self):
        self.a = "pythonforprogrammer"
        self.__c = "python for programmer"

class derived(Base):
    def __init__(self):
        Base.__init__()
        print("calling private member of base class")
        print(self.__c)

obj1 = Base()
print(obj1.a)
print(obj1.c)

obj2 = derived()

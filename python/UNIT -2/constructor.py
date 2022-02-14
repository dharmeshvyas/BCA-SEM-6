'''
The __init__ method is similar to constructors in C++ and Java.
It is run as soon as an object of a class is instantiated.
The method is useful to do any initialization you want to do with your object. 
'''

class Student:

    def __init__(self,id,name):
        self.id = id
        self.name = name

    
    def info(self):
        print("id : {}\nname :{}".format(self.id,self.name))
    

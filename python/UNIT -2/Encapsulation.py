class Student:
    __id = 0
    def __init__(self,name,roll):
        Student.id+=1
        self.name = name
        self.roll = roll

    def __str__(self):
        return "Name : {}\nRoll no : {}".format(self.name,self.roll)

st0 = Student('dharmesh',71)

#print(st0.id)
#above example throw  error
print(st0)

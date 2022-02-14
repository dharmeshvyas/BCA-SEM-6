from multipledispatch import dispatch
class Student:

    def __init__(self,id=0,name=""):
        self.id = id
        self.name = name
    @dispatch()
    def info(self):
        print("id : {}\nname :{}".format(self.id,self.name))
    @dispatch(str)
    def info(self,div):
        print("id : {}\nname :{}\nDivison :{}".format(self.id,self.name,div))
        

stud0 = Student(71,'dhar')
stud0.info('A')

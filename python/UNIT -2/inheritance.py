from constructor import Student

class Std12(Student):

    def __init__(self,id,name,division):
        self.division = division
        super().__init__(id,name)
        

    def info(self):
        print("id : {}\nName : {}\nDivision : {}".format(self.id,self.name,self.division))

        
me = Std12(71,"Dharmesh","A")
me.info()

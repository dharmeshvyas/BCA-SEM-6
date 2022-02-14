class Parrot:
    species = "bird"
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    
    def __str__(self):
        return"{}(name:{} age :{})".format(__class__.species,self.name,self.age)


blu = Parrot("Blu",10)
woo = Parrot("woo",21)

print(blu)
print(woo)

class Perrot:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sing(self,song):
        return "{} sing {}..".format(self.name,song)

    def dance(self):
        return "{} is now dancing..".format(self.name)

peepo = Perrot('peepo',12)

print(peepo.sing("beatiful people"))
print(peepo.dance())

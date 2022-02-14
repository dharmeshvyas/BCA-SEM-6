class Bird:

    def __init__(self):
        print("Bird is ready!!!")

    def WhoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster......")

class Duck(Bird):

    def __init__(self):

        super().__init__()
        print("Duck is ready..")
        

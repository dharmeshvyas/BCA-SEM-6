class Bird:

    def __init__(self):
        print("Bird is ready!!!")

    def WhoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster......")

#child class
class Duck(Bird):

    def __init__(self):

        super().__init__()
        print("Duck is ready..")

    def whoisthis(self):
        print("Duck")

    def run(self):
        print("it can work")

duck = Duck()
duck.whoisthis()
duck.swim()
duck.run()

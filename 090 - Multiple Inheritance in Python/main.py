class Human:
    def __init__(self,hand) -> None:
        print(" calling init function Human")
        self.eyes = 2
        self.nose = 1
        self.hand = hand

    def eat(self):
        print("I am eating")
    
    def walk(self):
        print("I am walking human")

class Male:
    def __init__(self,name) -> None:
        print(" calling init function Male")
        self.name = name

    def male(self):
        print("I am a Male")

    def walk(self):
        print("I am walking male")

class Boy(Human,Male):
    def __init__(self,name,hand) -> None:
        print(" calling init function Boy")
        Male.__init__(self,name)
        Human.__init__(self,hand)

    def boy(self):
        print("I am a Boy")

    def info(self):
        print(f"name = {self.name} , hand = {self.hand}")

    # def walk(self):
    #     print("I am walking boy")

b1 = Boy("Amit",10)
b1.boy()
b1.male()
b1.eat()
b1.walk()

print("eyes",b1.eyes)
print("nose",b1.nose)
print("hand",b1.hand)

# Male.work(b1)

# mro - method resolution order
print(Boy.mro())

b1.info()
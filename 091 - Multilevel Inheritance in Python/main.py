class Human(object):
    def __init__(self,hand):
        self.hand = hand
    def eat(self):
        print("Human eats")
    def work(self):
        print("Human works")

class Male(Human):
    def __init__(self,name) -> None:
        self.name = name
    def sleep(self):
        print("Male sleeps")
    def work(self):
        print("Male works")

class Boy(Male):
    def __init__(self,name,hand) -> None:
        super().__init__(name)
        Human.__init__(self,hand)
    def work(self):
        print("Boy works")
    
    def info(self):
        print(f"name = {self.name} , hand = {self.hand}")

class Programmer(Boy):
    def work(self):
        print("Programmer works")

b1 = Boy("AMit",2)
b1.eat()
b1.sleep()
b1.work()

b1.info()

print(Boy.mro())
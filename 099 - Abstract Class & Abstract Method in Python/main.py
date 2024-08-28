from abstract_class import Vehicle

class Bike(Vehicle):
    def __init__(self,n,color) -> None:
        super().__init__(n)
        self.color = color
    def start(self):
        print("Start Bike")

class Scooty(Vehicle):
    def __init__(self,n) -> None:
        super().__init__(n)
    def start(self):
        print("Start Scooty")

class Car(Vehicle):
    def __init__(self,n) -> None:
        super().__init__(n)
    def start(self):
        print("Start Car")

b = Bike(2,"Red")
b.start()
b.show()

s = Scooty(2)
s.start()
s.show()
from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self,n) -> None:
        self.no_of_tyres = n

    @abstractmethod
    def start(self):
        pass

    def show(self):
        print("show Vehicle , tyres =",self.no_of_tyres)

# v = Vehicle(2)
# print(v.no_of_tyres)
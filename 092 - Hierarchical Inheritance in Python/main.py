class Human(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(" calling Human class")

    def eat(self):
        print("Human eat")
    
class Male(Human):
    def sleep(self):
        print("Male sleeps")

class Female(Human):
    def work(self):
        print("Female work")

f1 = Female("Amit",22)
f1.work()
f1.eat()
print("name :",f1.name)
print("age :",f1.age)

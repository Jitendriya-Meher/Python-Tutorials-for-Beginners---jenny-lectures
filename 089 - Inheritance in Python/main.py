class Human:
    def __init__(self,eyes,nose):
        self.eyes = eyes
        self.nose = nose

    def eat(self):
        print("I am Eating",self.eyes)
    def work(self):
        print("I am working",self.nose)

class Animal:
    def ani(self):
        print("I am an animal")

class Male (Human,Animal):
    def __init__(self,name,eyes,nose):
        self.name = name
        super().__init__(eyes,nose)

    def boys(self):
        print("I am a boy",self.name)
        super().work()

b1 = Male("Amit",2,1)
b1.eat()
b1.boys()
b1.ani()


#  object-oriented programming (OOP) that deals with bundling the data (attributes) and the methods (functions) that operate on the data into a single unit, typically a class. It also involves restricting access to certain components of an object, which helps in protecting the internal state of the object from unintended modification.

class Student:
    def __init__(self,name,rn,age):
        self.name = name
        self.rn = rn
        self.__age = age

    def dispay(self):
        print(f"Hi myself {self.name} from Student class , rollno. {self.rn}, age = {self.__age}")

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    def show(self):
        print(f"Hi myself {self.name} from Student class , rollno. {self.rn}, age = {self.__age}")

def showData(x):
    x.dispay()

s = Student("amit",1,22)
showData(s)

print(s.get_age())
s.set_age(23)
print(s.get_age())

showData(s)
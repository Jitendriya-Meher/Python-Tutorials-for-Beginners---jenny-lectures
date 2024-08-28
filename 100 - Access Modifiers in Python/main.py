class Student:
    def __init__(self,name,rn,age):
        self.name = name
        self.rn = rn
        self.__age = age

    def dispay(self):
        print(f"Hi myself {self.name} from Student class , rollno. {self.rn}, age = {self.__age}")

class Branch(Student):
    def show(self):
        print(f"Hi myself {self.name} from Student class , rollno. {self.rn}, age = {self.__age}")

def showData(x):
    x.dispay()

# s1 = Student("Rahul",2)
# s1.dispay()

# b1 = Branch("Amit",1)
# b1.dispay()
# b1.name = "AMIT"

# showData(s1)
# showData(b1)

b = Branch("AMit",1,21)
b.dispay()
# print(b.__age)
print(dir(b))

print("age = ",b._Student__age)
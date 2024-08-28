print(1+2)
print("1"+"2")

print(int.__add__(5,2))

print(str.__add__("Amit "," Meher"))


class ComplexNumber:
    def __init__(self,r,i):
        self.real = r
        self.imag = i

    def print(self):
        print(f" {self.real} + {self.imag}i")

    def __add__(self,other):
        r = self.real + other.real
        i = self.imag + other.imag
        return f" {r} + {i}i"

c1 = ComplexNumber(1,2)
c1.print()

c2 = ComplexNumber(3,3)
c2.print()

c3 = c1+c2
print(c3)
print(c1+c2)
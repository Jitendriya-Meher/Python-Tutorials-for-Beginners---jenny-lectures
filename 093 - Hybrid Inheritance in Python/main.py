class A:
    def show(self):
        print("show A")

class B(A):
    def show(self):
        print("show B")

class C:
    def show(self):
        print("show C")

class D(B,C):
    def show(self):
        print("show D")

d = D()
d.show()

print(D.mro())
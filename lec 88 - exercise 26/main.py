class Circle:
    def __init__(self,r):
        self.r = r
        self.area = 3.14 * r * r
        self.circ = 2 * 3.14 * r
    
    def print(self):
        print(f"radiuns = {self.r} , area = {self.area} , . circumference = {self.circ}")
    
c1 = Circle(1)
c2 = Circle(10)

c1.print()
c2.print()
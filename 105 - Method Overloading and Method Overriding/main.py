class Demo:
    def sum(self, x,y):
        return x+y
    def sum(self, x,y,a):
        return x+y+a
    def sum(self, x,y,a,b):
        return x+y+a+b
    
    def sum(self, x,y,a=0,b=0):
        return x+y+a+b
    
    def sum(self, *arr):
        total = 0
        for num in arr:
            total += num
        return total
    
d = Demo()
print(d.sum(1,2))
print(d.sum(1,2,3))
print(d.sum(1,2,3,4))

class Father:
    def sleep(self):
        print("Father sleep")
    def eat(self):
        print("Father sleep")

class Son(Father):
    # pass
    def sleep(self):
        print("Son sleep")

ram = Son()
ram.sleep()
ram.eat()
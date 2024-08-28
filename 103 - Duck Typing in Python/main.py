def square(x):
    return x*x

print(square(5))
print(square(5.5))


class Duck:
    def swim(self):
        print("I am a duck and i can swim")
    def speaks(self):
        print("Duck quack")

class Dog:
    def swim(self):
        print("I am a dog and i can swim")
    def speaks(self):
        print("woff woof")

class Person:
    def swim(self):
        print("I am a person and i can swim")


def display(obj):
    obj.swim()
    obj.speaks()
    print("Information displayed")

d = Duck()
dog = Dog()
p = Person()

display(d)
display(dog)
# display(p)
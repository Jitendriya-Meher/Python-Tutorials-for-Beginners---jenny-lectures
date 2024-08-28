from typing import Any


list1 = [1,23,3]

print(list1)
print(len(list1))
print(list1.__len__())

class Demo:
    name = "amit"

d = Demo()

# print(len(d))
print(len(d.name))
print(d.name.__len__())

print(d)
print(d.__class__)


class Author:
    def __init__(self,name,book,pages) -> None:
        self.name = name
        self.book = book
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __str__(self):
        return f"{self.book} by {self.name}"

    def __call__(self,*args,**kwargs):
        print("hii author is called")

    def __del__(self):
        print("author is deleted")
        
        
a = Author("Amit","Avengers",1290)
print(a)
print(len(a))
a()

del a

# print(a)
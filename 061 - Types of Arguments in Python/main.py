def greet( name, dept,subject="Maths"):
    print(f"hii {name}, from {dept} department, subject = {subject}")

greet("amit","CS")
greet(dept="ME",name="Biswa")

greet("Jiten",dept="CSE")
# greet(dept="CSE","Jiten")

greet("amit","CS","Science")
greet(dept="ME",name="Biswa",subject="english")

greet("Jiten",dept="CSE",subject="Hindi")


def add(*arr):
    sum = 0
    for val in arr:
        sum += val
    print("sum = ",sum)

add(1,2,3,4,5)
add(1,2,3,5)
add(1,2,)
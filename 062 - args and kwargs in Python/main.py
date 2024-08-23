def add (a, *nums):
    print(f"a = {a}")
    print(nums,type(nums))
    sum = 0
    for num in nums:
        sum += num
    print("sum = ",sum)

add(1)
add(1,2)
add(1,2,3,4,5,6,7,8,9,10,11,12,13,14)

def info ( **kwargs):
    print(kwargs,type(kwargs))
    print(f"name = {kwargs['name']} , dept = {kwargs['dept']}")

    for key,val in kwargs.items():
        print(f"{key} = {val}")

info(name="amit",dept="CSE",subject="Maths")


def fun (*args, **kwargs):
    print(args)
    print(kwargs)

fun(1,2,3,a=12,b=12)
def mul ( *args):
    ans = 1
    for val in args:
        ans *= val
    print(f"multiply = {ans}")

mul(1,2,3,4,5,6,7,8,9,10)
mul(1,2,3,4)
mul(-1,1,2,3,4,5)
import math

def cans_req (cover=7):
    h = int(input("Height = "))
    w = int(input("Width = "))
    cans = (h*w)/7
    cans = math.ceil(cans)
    print(f"cans rewqired = {cans}")

cans_req()
cans_req(5)
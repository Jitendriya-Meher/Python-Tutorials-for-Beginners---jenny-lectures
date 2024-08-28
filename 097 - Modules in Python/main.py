import data
# import myModule as m
from myModule import area_of_circle as AC , pi


print("data1 : ",data.data1)

d2 = data.data2
print("data2 : ",d2)

for d in d2:
    # print(d)
    # print(d2[d])
    print("name",d," = ",d2[d]["name"])


area1 = AC(10)
# pi = 3.14

print("Area a circle of radius 10 : ", area1)

print("pi = ",pi)
# print("pi = ",myModule.pi)
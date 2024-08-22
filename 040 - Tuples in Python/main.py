tuple1 = (12,'amit',True,12)
print(tuple1)
print(type(tuple1))
print(tuple1[2])
print(tuple1[-2])

tup2 = (10,)
print(tup2)
print(type(tup2))

tup3 = (10)
print(tup3)
print(type(tup3))

# tuple are immutable / unchangeable
# tuple1[0] = 10

print(tuple1[1:])
print(tuple1[:3])
print(tuple1[1:3])
print(tuple1[1::2])

tup4 = (tuple1,tup2)
print(tup4)
print(tup4[0])
print(len(tup4))

# tuple concartination
tup5 = (tuple1 + tup2)
print(tup5)
print(tup5[0])
print(len(tup5))

t = (12,3,4,5,-1)

print(max(t))
print(min(t))
print(t.count(3))

print(tuple([2,3,4]))
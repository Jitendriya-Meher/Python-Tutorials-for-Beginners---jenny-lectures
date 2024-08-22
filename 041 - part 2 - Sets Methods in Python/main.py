s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

print(s1)
print(s2)

print(s1.union(s2))
print(s1|s2)
# s1 |= s2

print(s1.intersection(s2))
print(s1&s2)
# s1 &= s2

print(s1.difference(s2))
print(s1-s2)
# s1 -= s2

print(s2.difference(s1))
print(s2-s1)

# s1.update(s2)
# print(s1) 

# s1.intersection_update(s2)
# print(s1) 
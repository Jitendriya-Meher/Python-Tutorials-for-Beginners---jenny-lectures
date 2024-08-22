s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8,9,10}

print(s1.difference(s2))
print(s1-s2)

print(s2.difference(s1))
print(s2-s1)

# s1.difference_update(s2)
# print(s1)

print(s1.symmetric_difference(s2))
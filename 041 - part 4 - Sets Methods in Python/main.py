s1 = {1,2,3,4,5}
s2 = {5,6,7,8,9}
s3 = {9,10,11,12,13,14,15,16,17}
s4 = {1,2}

print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

print(s4.issubset(s2))
print(s4.issubset(s1))
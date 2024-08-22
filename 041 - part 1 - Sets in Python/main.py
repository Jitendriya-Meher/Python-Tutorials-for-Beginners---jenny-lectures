s1 = {10,12,56,'amit',True,False,10,False}
print(s1)
print(type(s1))

# print(s1[0])

s2 = {}
print(s2)
print(type(s2))

# empty set 
s3 = set()
print(s3)
print(type(s3))

# add element to set 
s1.add(99)
print(s1)
print(len(s1))

# remove element from set 
s1.remove(99)
print(s1)

# s1.remove(11)
print(s1)

s1.discard(99)
print(s1)

s1.discard(True)
print(s1)

print(s1.pop())
print(s1)

s1.add((1,2,4))
print(s1)

# s1.add([1,2])
s1.add("amit meher")
print(s1)
a = 5
b = 5

print(a,b)
print(a is b)
# check memory location
print(a == b)
# check the value 
print(a is not b)

print(id(a))
print(id(b))

b = 6

print("\n",a,b)
print(a is b)
print(a == b)
print(a is not b)
print(id(a))
print(id(b))

print()

a = 5
b = 5.0

print(a,b)
print(a is b)
# check memory location
print(a == b)
# check the value 
print(a is not b)
print(id(a))
print(id(b))


print("\n",a,a)
print(a is a)
# check memory location
print(a == a)
# check the value 
print(a is not a)
for i in range (10):
    print(f"{i}",end=" ")

print()

for i in range (5,10):
    print(f"{i}",end=" ")

print()

for i in range (5,100,2):
    print(f"{i}",end=" ")

print()

r = range (5,100,5)
# r = range (5,100,5.2)
# r = range (5,100,0)
# step size must be interger and not be 0
for i in r:
    print(f"{i}",end=" ")

print()

for i in range( 15,-15,-2):
    print(f"{i}",end=" ")

sum = 0
for i in range (1,101):
    sum += i
print("\nsum 1 to 100 = ",sum)
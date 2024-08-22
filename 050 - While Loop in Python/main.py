count = 1

while ( count <= 5):
    print(count,end=" ")
    count += 1

print("\nwhile loop finished") 


count = 1

while ( count <= 5):
    print(count,end=" ")
    if(count == 3):
        break
    count += 1
else:
    print("\nwhile loop executed successfully",end="")

print("\nwhile loop finished") 


num = int(input("eneter a number (-1 to quit) : "))
arr = []
while ( num != -1):
    arr.append(num)
    num = int(input("eneter a number (-1 to quit) : "))
else:
    print("entered number :",arr)


total = 0
num = int(input("eneter a number ( 0 to quit ) : "))

while ( num != 0 ):
    total += num
    num = int(input("eneter a number ( 0 to quit ) : "))

print("total :",total)
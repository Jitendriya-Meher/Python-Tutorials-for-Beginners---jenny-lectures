# sum of digit of a number

a = "23"
print("sum =", int(a[0])+int(a[1]))

num = int(input("Enter a number : "))

sum = 0
temp = num

while( temp > 0):
    sum += temp%10
    temp = int(temp/10)

print("sum of digits = ", sum)

sum = 0
temp = str(num)
length = len(temp)

for i in range(length):
    sum += int(temp[i])
    
print("sum of digits = ", sum)
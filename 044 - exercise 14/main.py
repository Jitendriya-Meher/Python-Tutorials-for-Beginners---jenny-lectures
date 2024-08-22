# lists = [151,153,160,143]
ip = input("Enter the height sep by , : ")
lists = ip.split(" ")

sum = 0
length = 0

for val in lists:
    sum += int(val)
    length += 1

avg = round(sum / length)

print("Average :",avg)
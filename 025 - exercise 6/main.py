# check a number is even or odd

num = int(input("Enter a number : "))

# modulo 
if ( num%2 == 0):
    print("This is an even number")
else:
    print("This is a odd number")


# and with 1
if ( num&1 == 0):
    print("This is an even number")
else:
    print("This is a odd number")
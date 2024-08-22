bill = 0

size = input("What size pizza you want (S/M/L) : ")

if ( size == "S" or size == "s"):
    bill += 100
elif ( size == "M" or size == "m"):
    bill += 200
elif ( size == "L" or size == "l"):
    bill += 300
else:
    print("Wrong size of pizza")

add_pepperoni = input("Do you want to add a pepperoni (y/n) : ")

if ( add_pepperoni == "y" or add_pepperoni == "Y"):
    if( size == "S" or size == "s"):
        bill += 30
    else:
        bill+=50

extra_cheese = input("Do you want extra cheese (Y/n) : ")

if ( extra_cheese == "Y" or extra_cheese == "y"):
    bill += 20

print(f"Your bill : {bill}")
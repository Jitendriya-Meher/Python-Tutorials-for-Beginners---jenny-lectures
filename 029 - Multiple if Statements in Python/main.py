height = float( input("Enter height : "))
bill = 0

if height >= 3 :
    print("can ride")

    age = int(input("Enter age : "))

    if age < 12 :
        bill = 150
    elif age < 18 :
        bill = 250
    else:
        bill = 500

    want_photo = input("Do you want to take photo (y/n): ")

    if want_photo == 'y' or want_photo == 'Y' :
        bill += 50

    print(f"total bill : {bill}")

else :
    print("can't ride")

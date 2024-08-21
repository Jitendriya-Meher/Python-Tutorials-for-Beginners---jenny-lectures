weight = int(input("Enter the weight in Kg : "))
height = float(input("Enter the height in meters : "))

bmi = weight / ( height**2 ) 
bmi = int(bmi)

print("BMI : ", bmi)

# int shuld be in base 10
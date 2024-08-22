weight = float(input("Enter Weight: "))
height = float(input("Enter Height: "))

bmi = weight / ( height ** 2)
print("BMI: ", bmi)

bmi = round(bmi,1)
print("BMI: ", bmi)

if bmi < 18.5 :
    print(f"your BMI is {bmi} and you are underweight")
elif bmi < 25 :
    print(f"your BMI is {bmi} and you have a normal weight")
elif bmi < 30 :
    print(f"your BMI is {bmi} and you are overweight")
elif bmi < 35 :
    print(f"your BMI is {bmi} and you are Obese")
else :
    print(f"your BMI is {bmi} and you are clically Obese")
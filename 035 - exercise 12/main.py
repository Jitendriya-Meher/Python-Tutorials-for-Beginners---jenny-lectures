import random

names = input("Enter names separated by commas : ")

names_list = names.split(",")
print(names_list)

b1 = random.choice(names_list)
print(f"{b1} will pay the bill first")

b2 = names_list[random.randint(0,len(names_list)-1)]
print(f"{b2} will pay the bill second")
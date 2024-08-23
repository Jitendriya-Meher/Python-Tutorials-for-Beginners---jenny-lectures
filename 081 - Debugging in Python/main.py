
def dispay():
    for i in range(1,11):
        if(i==10):
            print("Byee!!")

dispay()


import random

dice_nums = ["one", "two", "three", "four", "five", "six"]
roll = random.randint(0,5)
print("dice = ",dice_nums[roll])
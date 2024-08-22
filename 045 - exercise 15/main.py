# max and min in a list 

arr = [12,13,1,3,4,5,111,7,8,99999,9,0,-11]

mini = maxi = arr[0]

for val in arr:
    if( val > maxi ):
        maxi = val
    if( val < mini ):
        mini = val

print("max = ", maxi)
print("min = ", mini)
nums = [1,2,3,4,5,6,7,8,9,10,-1,-2]
print(nums)

names = ["amit","jiten","somya","adi"]
print(names)

mix_list = [1,2,"jiten",21.21,True,False]
print(mix_list)

print(mix_list[0])
print(mix_list[3])
print(mix_list[-1])
print(mix_list[-3])

# print(mix_list[8])
# list index out of bound

# list slicing
# list[starting index : ending index : steps]
print(mix_list[1:4])
print(mix_list[2:-1])
print(mix_list[2:])
print(mix_list[-2:])
print(mix_list[-3:-1])

print(mix_list[1:6:1])
print(mix_list[1:6:2])
print(mix_list[1:6:3])

# sorting
print(nums)
nums.sort()
print(nums)

# reverse
nums.reverse()
print(nums)

# min , max
print(min(nums))
print(max(nums))

# add to list 
# at end 
nums.append(-100)
print(nums)

# any position 
# list.insert( position , value) 
nums.insert(1,-20)
print(nums)

# at end ( list )
nums.extend([11,12,13])
print(nums)

nums[1] = 121
print(nums)

nums[1:4] = [111,112,113]
print(nums)

# remove elements 

# list.remove(value)
# remove the first occurrence
nums.remove(10)
print(nums)

# remove last element
print(nums.pop())
print(nums)
# list.pop(index)
print(nums.pop(1))
print(nums)

# count the occurrences of an element
print(nums.count(-2))

# clear a list
nums.clear()
print(nums)
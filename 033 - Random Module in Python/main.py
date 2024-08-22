import random

# end included
print(random.randint(1,10))

# between 0-1
print(random.random())

# end excluded
print(random.randrange(1,10))

# in between start and end
print(random.uniform(1,3))


l = [1,5,6,2,-1,3,4,5,6]
print(random.choice(l))

random.shuffle(l)
print(l)
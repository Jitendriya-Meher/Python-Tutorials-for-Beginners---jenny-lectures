name1 = input("Enter his name : ")
name2 = input("Enter her name : ")

name = name1 + name2
name = name.lower()

score = 0
total = ''

score += name.count('t')
score += name.count('r')
score += name.count('u')
score += name.count('e')

total += str(score)
score = 0

score += name.count('l')
score += name.count('o')
score += name.count('v')
score += name.count('e')

total += str(score)

print(f"your love score is {total}")
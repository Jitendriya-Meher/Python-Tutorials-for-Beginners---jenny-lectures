list = [
    ['😎','😎','😎'],
    ['😎','😎','😎'],
    ['😎','😎','😎'],
]

print(list)

row = int(input("Enter row number: "))
col = int(input("Enter column number: "))

row -= 1
col -= 1

list[row][col] = '🔍'

print(list)
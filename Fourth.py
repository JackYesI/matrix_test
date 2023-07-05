import random

matrix = []

row = int(input("Enter row: "))

for i in range(row):
    matrix.append(random.randint(1,100))

print(matrix)
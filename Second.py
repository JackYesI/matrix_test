import random

matrix = []

row = int(input("Enter row: "))

for i in range(row):
    matrix.append(random.randint(1,100))

print(matrix)
   
for i in range(0,row, 2):
    if i + 1 >= row:
        break
    x = matrix[i]
    matrix[i] = matrix[i + 1]
    matrix[i + 1] = x

print(matrix)
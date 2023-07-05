import random

matrix = []

row = int(input("Enter row: "))

for i in range(row):
    matrix.append(random.randint(1,100))
   
max = max(matrix)
min = min(matrix)

max_i = matrix.index(max)
min_i = matrix.index(min)

print(matrix)

if min_i > max_i:
    for i in range(max_i + 1,min_i):
        matrix[i] = matrix[i] * 2
elif max_i > min_i:
    for i in range(min_i + 1,max_i):
        matrix[i] = matrix[i] * 2

print(matrix)

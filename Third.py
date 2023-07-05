import random

matrix = []

row = int(input("Enter row: "))

for i in range(row):
    matrix.append(random.randint(1,100))

print(matrix)
print("repetition --> ", end='')

for i in matrix:
    count = matrix.count(i)
    if count > 1:
        print("{}, ".format(i), end='') 
        while count != 0:
            count -= 1
            matrix.remove(i)   
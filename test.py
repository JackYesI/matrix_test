
# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# for item in matrix:
#     for li in item:
#         print(li, end='\t')
#     print()
 
#####################################

# import random

# matrix = []

# row = 3
# col = 3

# for i in range(row):
#     list_row = []
#     for j in range(col):
#         list_row.append(random.randint(10,50))
#     matrix.append(list_row)
#     col += 1

# print(matrix)

# for item in matrix:
#     for li in item:
#         print(li, end='\t')
#     print()

# print('len matrix :: ',len(matrix))
# sum_ = 0
# for item in matrix:
#     print('list len :: ', len(item))
#     sum_ += sum(item)

# print("sum :: ", sum_)

#######################################

import random

matrix = []

row = int(input("Enter row: "))

for i in range(row):
    list_row = []
    for j in range(row):
        list_row.append(random.randint(1,100))
    matrix.append(list_row)

print(matrix)

sum_1 = 0
sum_2 = 0

for i in range(row):
    sum_1 = sum_1 + matrix[i][i]
    sum_2 = sum_2 + matrix[i][row - 1 - i]

for item in matrix:
    for li in item:
        print(li, end='\t')
    print()

print('sum for diagonal',sum_1)
print('sum for bichna diagonal', sum_2)

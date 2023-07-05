import random

matrix = []
sum_list = []

row = random.randint(1,10)
col = random.randint(1,10)

for i in range(row):
    list_row = []
    for j in range(col):
        list_row.append(random.randint(1,100))
    matrix.append(list_row)

print(matrix)
sum_row = 0


for i in range(row):
    for j in range(col):
        print(matrix[i][j], end='\t')
        sum_row += matrix[i][j]
        if i == 0:
            sum_list.append(matrix[i][j])
        else:
            sum_list[j] += matrix[i][j]
    print(' | ',sum_row)
    sum_row = 0
print('-' * 100)

for item in sum_list:
    print(item, end='\t')


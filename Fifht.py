
matrix = list()

for i in range(8):
    list_row = list()
    for j in range(8):
        list_row.append('-')
    matrix.append(list_row)

row_t = int(input("row T: "))
col_t = int(input("col T: "))

matrix[row_t][col_t] = 'T'

for i in range(8):
    for j in range(8):
        if j == col_t or i == row_t:
            if j == col_t and i == row_t:
                continue
            matrix[i][j] = '*'

for item in matrix:
    for li in item:
        print(li, end='\t')
    print()
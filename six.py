
matrix = list()

for i in range(8):
    list_row = list()
    for j in range(8):
        list_row.append('-')
    matrix.append(list_row)

row_o = int(input("row O: "))
col_o = int(input("col O: "))

matrix[row_o][col_o] = 'O'

if col_o > row_o:
    start = col_o - row_o
    start_j = 8 - (col_o + 1)
    subtractor = start_j - row_o
    for i in range(8):
        for j in range(8):
            if i == j - start or j == 7 - subtractor - i:
                if j == col_o and i == row_o:
                    continue
                matrix[i][j] = '*'
elif col_o < row_o:
    start = row_o - col_o
    start_j = 8 - (row_o + 1)
    subtractor = start_j - col_o
    for i in range(8):
        for j in range(8):
            if j == i - start or i == 7 - subtractor - j:
                if j == col_o and i == row_o:
                    continue
                matrix[i][j] = '*' 

for item in matrix:
    for li in item:
        print(li, end='\t')
    print()

matrix = list()

for i in range(8):
    list_row = list()
    for j in range(8):
        list_row.append('-')
    matrix.append(list_row)

row_h = int(input("row H: "))
col_h = int(input("col H: "))

matrix[row_h][col_h] = 'H'

if 0 <= row_h - 2 <= 7 and 0 <= col_h - 1 <= 7:
    matrix[row_h - 2][col_h - 1] = '*'
if 0 <= row_h - 1 <= 7 and 0 <= col_h - 2 <= 7:
    matrix[row_h - 1][col_h - 2] = '*'
if 0 <= row_h - 2 <= 7 and 0 <= col_h + 1 <= 7:
    matrix[row_h - 2][col_h + 1] = '*'
if 0 <= row_h - 1 <= 7 and 0 <= col_h + 2 <= 7:
    matrix[row_h - 1][col_h + 2] = '*'
if 0 <= row_h + 2 <= 7 and 0 <= col_h - 1 <= 7:
    matrix[row_h + 2][col_h - 1] = '*'
if 0 <= row_h + 1 <= 7 and 0 <= col_h - 2 <= 7:
    matrix[row_h + 1][col_h - 2] = '*'
if 0 <= row_h + 2 <= 7 and 0 <= col_h + 1 <= 7:
    matrix[row_h + 2][col_h + 1] = '*'
if 0 <= row_h + 1 <= 7 and 0 <= col_h + 2 <= 7:
    matrix[row_h + 1][col_h + 2] = '*'

for item in matrix:
    for li in item:
        print(li, end='\t')
    print()
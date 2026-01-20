#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 9

import random

matrix = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(random.randint(0, 1))
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)

max_ones_row = 0
max_row_index = 0
for i in range(4):
    count = matrix[i].count(1)
    if count > max_ones_row:
        max_ones_row = count
        max_row_index = i

max_ones_col = 0
max_col_index = 0
for j in range(4):
    count = sum(matrix[i][j] for i in range(4))
    if count > max_ones_col:
        max_ones_col = count
        max_col_index = j

print("Row with most 1s:", max_row_index)
print("Column with most 1s:", max_col_index)

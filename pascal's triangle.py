# pascals triagle
row = 4
col = 4

triangle_matrix = [[0 for i in range(col)] for j in range(row)]

for i in range(row):
    for j in range(col):
        if i == 0 or j == 0:
            triangle_matrix[i][j] = 1

for i in range(1,row):
    for j in range(1, col):
        triangle_matrix[i][j] = triangle_matrix[i - 1][j] + triangle_matrix[i][j - 1]

for i in range(row):
    for j in range(col):
        print(triangle_matrix[i][j], end = " ")
    print()

print()
"""
j = col -1
for i in range(row):
    print(triangle_matrix[i][j], end = " ")
    j -= 1
print()

"""

print()
row = 0
col = 0
while col < 4:
    j = col
    for i in range(row+1):                          # what if we use range(row)?
        print(triangle_matrix[i][j], end = " ")   # then at very first iteration i = range(0) and j = 0 , so
        j -= 1                                  # matrix[0, 0] would be ignored and at every other iteration
    print()                                   # the last element or 1 would be ignored because range() function
    row += 1                                 # always counts one less than the given number.
    col += 1
print()
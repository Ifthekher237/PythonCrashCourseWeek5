import random
from typing import List, Any, Union


def matrix(m, n):
    make_matrix = []
    for i in range(m):
        col = []
        for j in range(n):
            get = random.randint(0, m * n)
            col.append(get)
        make_matrix.append(col)
    return make_matrix


def matrixSum(a, b):
    for i in range(row):
        for j in range(col):
            print("{:2d}".format(a[i][j] + b[i][j]), end=" ")
        print()


def matrix_print(mat):
    for i in range(row):
        for j in range(col):
            print(mat[i][j], end=" ")
        print()


global row
row = int(input("row: "))
global col
col = int(input("col: "))

a = matrix(row, col)
b = matrix(row, col)

matrix_print(a)
print()
matrix_print(b)

print()

matrixSum(a, b)

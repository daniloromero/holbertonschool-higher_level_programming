#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_x = [[j ** 2 for j in i] for i in matrix]
    return matrix_x

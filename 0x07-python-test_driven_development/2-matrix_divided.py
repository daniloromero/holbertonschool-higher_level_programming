#!/usr/bin/python3
""" Module for division of  all elements of a matrix"""


def matrix_divided(matrix, div):
    """ function that divides all elements of a matrix
    Arguments:

    matrix: must be a list of lists of integers or floats
    Each row of the matrix must be of the same size

    div: must be a number (integer or float), div can’t be equal to 0

    Returns a new matrix, elements rounded to 2 decimal places

    Raise TypeError or ZeroDivisionError when needed
    """
    if type(matrix) != list:
        raise TypeError('matrix must be a matrix (list of lists) of \
                            integers/floats')

    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of  \
                            integers/floats")

    checklen = [len(i) for i in matrix]
    if len(set(checklen)) != 1:
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError('division by zero')

    div_matrix = [[round(h / div, 2)for h in i]for i in matrix]
    return div_matrix

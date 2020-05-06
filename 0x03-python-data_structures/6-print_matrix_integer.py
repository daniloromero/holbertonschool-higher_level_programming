#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        whitespace = ""
        for j in i:
            print("{:s}{:d}".format(whitespace, j), end="")
            whitespace = " "
        print()

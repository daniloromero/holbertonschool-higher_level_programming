#!/usr/bin/python3
""" Function to add 2 integers """


def add_integer(a, b=98):
    """ function definition """
    result = 0

    """ Raise TypeError Exception """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        result = int(a) + int(b)
    return result

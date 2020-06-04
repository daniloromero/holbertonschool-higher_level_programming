#!/usr/bin/python3


def pascal_triangle(n):
    """list of lists of integers representing the Pascal’s triangle of n"""
    if n <= 0:
        return ([])

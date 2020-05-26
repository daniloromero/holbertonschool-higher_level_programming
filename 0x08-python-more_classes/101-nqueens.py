#!/usr/bin/python3
""" The N queens puzzle backtracking """
import sys


class Nqueen:
    """that solves the N queens problem"""
    def __init__(self, n):
        """Initialization o attributes"""
        self.n = n
        self.answer = []


#Main

if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
if argv[1].isdigit() is False:
    print('N must be a number')
    exit(1)
if argv[1].isdigit() is True:
    n = int(argv[1]
if n < 4:
    print('N must be at leat 4')
    exit(1)

queen = Nqueen(n)



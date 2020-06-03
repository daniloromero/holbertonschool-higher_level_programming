#!/usr/bin/python3
"""Reads n lines form text file """


def read_lines(filename="", nb_lines=0):
    """function reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='UTF-8') as myfile:
        lines = myfile.readlines()
        if nb_lines <= 0 or nb_lines > len(lines):
            [print(i, end='') for i in lines]
        else:
            [print(lines[i], end='') for i in range(0, nb_lines)]

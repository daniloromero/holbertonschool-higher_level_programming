#!/usr/bin/python3
"""Get number of lines of text file """


def number_of_lines(filename=""):
    """Method returns # lines of a text file"""
    with open(filename) as Myfile:
        num_lines = len(Myfile.readlines())
        return num_lines

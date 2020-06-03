#!/usr/bin/python3


def number_of_lines(filename=""):
    """Mehtod returns # lines of a text file"""
    with open(filename) as Myfile:
        num_lines = len(Myfile.readlines())
        return num_lines

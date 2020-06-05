#!/usr/bin/python3
""" inserts line of text to file after each line containing  specific string"""


def append_after(filename="", search_string="", new_string=""):
    """appneds line of text"""
    with open(filename, "r") as myfile:
        lines = myfile.readlines()
        newlines = ""
        for i in range(len(lines)):
            newlines += lines[i]
            if search_string in lines[i]:
                newlines += new_string
    with open(filename, "w") as myfile:
        myfile.write("".join(newlines))

#!/usr/bin/python3
"""Class Mylist"""


class MyList(list):
    """Class that inherts form class list"""
    def print_sorted(self):
        """method that prints the list, but sorted (ascending sort)"""
        print(sorted(self))

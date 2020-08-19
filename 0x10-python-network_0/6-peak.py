#!/user/bin/python3
"""Finds a peak in a list of unsorted integerss"""


def find_peak(list_of_integers):
    """Finds peak number"""
    if len(list_of_integers) != 0:
        list_of_integers.sort()
        return (list_of_integers[-1])

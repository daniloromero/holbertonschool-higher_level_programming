#!/user/bin/python3
"""Finds a peak in a list of unsorted integerss"""


def find_peak(list_of_integers):
    """Finds peak number"""
    if len(list_of_integers) != 0:
        sortl = sorted(list_of_integers)
        return (sortl[-1])

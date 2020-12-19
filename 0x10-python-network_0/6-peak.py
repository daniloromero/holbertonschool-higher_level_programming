#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """find peak in list_of_integers"""
    if len(list_of_integers) == 0:
        return None
    else:
        list_of_integers.sort()
        return list_of_integers[-1] 


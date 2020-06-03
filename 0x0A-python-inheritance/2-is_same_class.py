#!/usr/bin/python3
""" Verifies for instance of a class"""


def is_same_class(obj, a_class):
    """method returns True if the object is exactly an instance
    of the specified class ; otherwise False"""
    return(type(obj) == a_class)

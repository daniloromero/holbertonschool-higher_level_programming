#!/usr/bin/python3
""" Vefifies if object is instance of a class or superclass"""


def is_kind_of_class(obj, a_class):
    """method that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False
    """
    return isinstance(obj, a_class)

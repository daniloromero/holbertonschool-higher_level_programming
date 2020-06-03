#!/usr/bin/python3
"""Verifies instance"""


def inherits_from(obj, a_class):
    """that returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ;
    otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return (type(obj) == a_class)

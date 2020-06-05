#!/usr/bin/python3


def add_attribute(self, attr, value):
    """method adds a new attribute to an object if it’s possible"""
    if not hasattr(self, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(self, attr, value)

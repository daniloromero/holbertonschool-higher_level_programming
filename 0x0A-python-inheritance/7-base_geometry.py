#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """Public instance method not implemented"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Value validation, name always is a string """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

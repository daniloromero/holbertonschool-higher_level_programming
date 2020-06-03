#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """Public instance method not implemented"""
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Value validation, name always is a string """
        if type(value) != int:
            raise TypeError('<name> must be an integer')
        elif value < 0:
            raise ValueError('<name> must be greater than 0')

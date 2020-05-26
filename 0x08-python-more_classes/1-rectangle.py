#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Class constructor for a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """ Private attribute getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private attribute setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """ Private attribute getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private attribute setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

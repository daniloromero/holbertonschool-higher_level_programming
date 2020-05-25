#!/usr/bin/python3
class Rectangle:
    """Class constructor for a Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Private attribute getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Private attribute setter """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self, value):
        """ Private attribute getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Private attribute setter """
        if type(value) != int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """ Public method for area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Public method for perimenter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

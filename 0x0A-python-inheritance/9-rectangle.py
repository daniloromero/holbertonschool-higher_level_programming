#!/usr/bin/python3

""" Class Rectanlge  inherits from BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Subclass Rectangle inherits form BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Method for area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ str method for rectangle """
        rectgl = "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
        return rectgl

#!/usr/bin/python3


"""Class Square that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Subclass Square inherits from Rectangle """
    def __init__(self, size):
        """ Constructor """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

#!/usr/bin/python3
""" class Square """


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for h in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("{}{}".format(" " * self.position[0],"#" * self.__size))

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (value != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] != int and value[1] != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

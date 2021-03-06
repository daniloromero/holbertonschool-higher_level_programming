#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Class constructor for a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
    def height(self):
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
        return self.width * self.height

    def perimeter(self):
        """ Public method for perimenter of Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ str method for a Rectangle """
        rectgl = ""
        if self.__width == 0:
            return rectgl
        else:
            for i in range(self.__height):
                rectgl += str(self.print_symbol) * self.__width
                if i != (self.__height - 1):
                    rectgl += "\n"
        return rectgl

    def __repr__(self):
        """ repr method, returns object representation as string """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Class Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method to get the bigger rectangle of a comparison"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """method to create a square Rectangle"""
        return cls(size, size)

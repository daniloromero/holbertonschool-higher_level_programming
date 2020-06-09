#!/usr/bin/python3
""" Class Rectangle inherits from base """
from models.base import Base


class Rectangle(Base):
    """Class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """method for area of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for h in range(0, self.y):
            print('')
        for i in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)

    def __str__(self):
        """overriding __str__ method returnS:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        rctgl = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        rctgl = rctgl.format(self.id, self.x, self.y, self.width, self.height)
        return rctgl

    def update(self, *args, **kwargs):
        """public method assigns an argument to each attribute"""
        attrlist = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) != 0:
            for i, value in enumerate(args):
                if i <= len(args):
                    setattr(self, attrlist[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary representation of Square """
        rctgldic = {"id": self.id, "width": self.width, "height": self.height,
                    "x": self.x, "y": self.y}
        return rctgldic

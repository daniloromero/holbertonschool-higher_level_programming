#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class initialization method """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """width getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """String method"""
        squr = "[Square] ({:d}) {:d}/{:d} - {:d}"
        squr = squr.format(self.id, self.x, self.y, self.size)
        return squr

    def update(self, *args, **kwargs):
        """Update attributes of Square"""
        attrlist = ['id', 'size', 'x', 'y']
        if args and len(args) != 0:
            for i, value in enumerate(args):
                if i <= len(args):
                    setattr(self, attrlist[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns dicitionary representation of Square """
        sqdic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return sqdic

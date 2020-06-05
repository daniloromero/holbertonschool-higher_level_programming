#!/usr/bin/python3
""" Class Myint that inherits form int """


class MyInt(int):
    """Class Myint is rebel has == and != operators inverted"""
    def __init__(self, num):
        self.num = num

    def __eq__(self, num):
        """ Call to Not equal method """
        return super().__ne__(num)

    def __ne__(self, num):
        """  Call to equal method """
        return super().__eq__(num)

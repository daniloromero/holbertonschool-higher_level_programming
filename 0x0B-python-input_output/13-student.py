#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """ Constructor method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method for class dictionary, If attrs is a list of strings,
        only attribute names contained in this list must be retrieved """
        if type(attrs) == list and all(type(i) for i in attrs):
            dic = {j: self.__dict__[j] for j in attrs if j in self.__dict__}
            return dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Method  replaces all attributes of the Student instance"""
        for i in json:
            self.__dict__[i] = json[i]

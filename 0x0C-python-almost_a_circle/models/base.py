#!/usr/bin/python3
""" Base Class"""
import json
import os
import csv


class Base:
    """Class Definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method for the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = cls.__name__ + ".json"
        if list_objs is None or list_objs == []:
            jsonstr = '[]'
        else:
            jsonstr = cls.to_json_string([i.to_dictionary()
                                          for i in list_objs])
        with open(filename, 'w') as jfile:
            jfile.write(jsonstr)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string """
        liststr = []
        if json_string is None or len(json_string) == 0:
            return liststr
        else:
            liststr = json.loads(json_string)
            return liststr

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        if dictionary is not None and len(dictionary) != 0:
            dummy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = cls.__name__ + ".json"
        list3 = []
        if os.path.isfile(filename):
            with open(filename, 'r') as jfile:
                list1 = jfile.read()
                list2 = cls.from_json_string(list1)
            for i in list2:
                list3.append(cls.create(**i))
        return list3

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ writes the seriarization of list_objs to a csv file """
        filename = cls.__name__ + ".csv"
        csvstr = '[]'
        if list_objs:
            csvstr = [i.to_dictionary() for i in list_objs]
        with open(filename, 'w') as csvfile:
            if cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == 'Square':
                fields = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()
            writer.writerows(csvstr)

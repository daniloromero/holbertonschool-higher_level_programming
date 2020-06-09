#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path


class TestBase(unittest.TestCase):
    """Test base unistest"""
    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0


    def test_id(self):
        """test id attribute"""
        b1 = Base(1)
        self.assertEqual(b1.id, 1)
        b2 = Base(2)
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 1)
        b4 = Base(12)
        self.assertEqual(b4.id, 12)
        b5 = Base (-12)
        self.assertEqual(b5.id, -12)


    def test_type(self):
        """Test for type and instance."""

        b = Base()
        self.assertEqual(type(b), Base)
        b1 = Base(1)
        self.assertTrue(type(b1), Base)

    def test_None(self):
        """Test for None as id argument"""
        b1 = Base(None)
        self.assertEqual(b1.id, 1)
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_base(self):
        """Test if is instance of class"""
        b1 = Base()
        self.assertTrue(isinstance(b1, Base))

    def test_rectnagle(self):
        """Test if Rectangle is instance of superclass"""
        r = Rectangle(3, 2)
        self.assertTrue(isinstance(r, Base))

    def test_square(self):
        """Test if Square is instnace of superclass"""
        s = Square(3)
        self.assertTrue(isinstance(s, Base))

    def test_tojson_string1(self):
        """ None or empty list of to_json_string method"""

        list1 = None
        json1 = Base.to_json_string(list1)
        self.assertEqual(json1, "[]")
        self.assertEqual(type(json1), str)

        list2 = []
        json2 = Base.to_json_string(list2)
        self.assertEqual(json2, "[]")
        self.assertEqual(type(json2), str)

    def test_tojson_string2(self):
        """list with empty dictionary of to_json_string"""
        list1 = [{}]
        json1 = Base.to_json_string(list1)
        self.assertEqual(json1, "[{}]")
        self.assertEqual(type(json1), str)

    def test_tojson_string3(self):
        """List with 1 dictionary element"""
        list2 = [{'x': 1, 'y': 2}]
        json2 = Base.to_json_string(list2)
        string = str(list2)
        self.assertEqual(json2, string.replace("'", "\""))
        self.assertEqual(type(json2), str)

    def test_tojson_string4(self):
        """list with 2 dictionary elements"""
        list1 = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]
        json1 = Base.to_json_string(list1)
        string = str(list1)
        self.assertEqual(json1, string.replace("'", "\""))
        self.assertEqual(type(json1), str)

if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
""" Unittest for square class
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path, remove
from unittest.mock import patch


class Test_argsS(unittest.TestCase):
    """ Class for unittest of arguments """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_no_size(self):
        """ Test for no width """
        with self.assertRaises(TypeError):
            s = Square()

    def test_no_x(self):
        """ Test for no x """
        s = Square(1)
        self.assertEqual(s.x, 0)

    def test_no_y(self):
        """ Test for no y """
        s = Square(1, 1)
        self.assertEqual(s.y, 0)

    def test_no_id(self):
        """ Test for no id """
        s = Square(1, 1, 1)
        self.assertEqual(s.id, 1)

    def test_id(self):
        """ Test for id """
        s = Square(1, 1, 1, 89)
        self.assertEqual(s.id, 89)

    def test_extra_arg(self):
        """ Test for no extra arguments """
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_size_positive(self):
        """ Positive Int for size """
        s = Square(3)
        self.assertEqual(s.size, 3)

    def test_size_negative(self):
        """ Negative Int for size """
        with self.assertRaises(ValueError):
            s = Square(-3)

    def test_size_zero(self):
        """ Zero for size """
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_width_float(self):
        """ positive float for size """
        with self.assertRaises(TypeError):
            s = Square(1.0)

    def test_size_float_negative(self):
        """ negative float for size """
        with self.assertRaises(TypeError):
            s = Square(-1.0)

    def test_size_None(self):
        """ None for size """
        with self.assertRaises(TypeError):
            s = Square(None)

    def test_width_string(self):
        """ String for size """
        with self.assertRaises(TypeError):
            s = Square("1")

    def test_width_list(self):
        """ List for size """
        with self.assertRaises(TypeError):
            s = Square([1])

    def test_width_tuple(self):
        """ Tuple for size """
        with self.assertRaises(TypeError):
            s = Square((1, ))

    def test_width_set(self):
        """ Set for size """
        with self.assertRaises(TypeError):
            s = Square({1})

    def test_x_positive(self):
        """ Positive Int for x """
        s = Square(1, 5)
        self.assertEqual(s.x, 5)

    def test_x_negative(self):
        """ Negative for x """
        with self.assertRaises(ValueError):
            s = Square(1, -5)

    def test_x_zero(self):
        """ Zero for x """
        s = Square(1, 0)
        self.assertEqual(s.x, 0)

    def test_x_float(self):
        """ positive float for x """
        with self.assertRaises(TypeError):
            s = Square(1, 1.0)

    def test_x_float_negative(self):
        """ negative float for x """
        with self.assertRaises(TypeError):
            s = Square(1, -1.0)

    def test_x_None(self):
        """ None for x """
        with self.assertRaises(TypeError):
            s = Square(1, None)

    def test_x_string(self):
        """ String for x """
        with self.assertRaises(TypeError):
            s = Square(1, "1")

    def test_x_list(self):
        """ List for x """
        with self.assertRaises(TypeError):
            s = Square(1, [1])

    def test_x_tuple(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            s = Square(1, (1, ))

    def test_x_set(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            s = Square(1, {1})

    def test_y_positive(self):
        """ Positive  for y """
        s = Square(1, 1, 5)
        self.assertEqual(s.y, 5)

    def test_y_negative(self):
        """ Negative  for y """
        with self.assertRaises(ValueError):
            s = Square(1, 1, -5)

    def test_y_zero(self):
        """ Zero Int for y """
        s = Square(1, 1, 0)
        self.assertEqual(s.y, 0)

    def test_y_float(self):
        """ positive float for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1.0)

    def test_y_float_negative(self):
        """ negative float for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, -1.0)

    def test_y_None(self):
        """ None for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, None)

    def test_y_strring(self):
        """ String for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, "1")

    def test_y_list(self):
        """ List for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, [1])

    def test_y_tuple(self):
        """ Tuple for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, (1, ))

    def test_ySetS(self):
        """ Set for y """
        with self.assertRaises(TypeError):
            s = Square(1, 1, {1})

    def test_area1(self):
        """Test Area Method """
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_area2(self):
        """Test Area Method """
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_area3(self):
        """Test Area Method """
        s = Square(3, 1, 1, 1)
        self.assertEqual(s.area(), 9)

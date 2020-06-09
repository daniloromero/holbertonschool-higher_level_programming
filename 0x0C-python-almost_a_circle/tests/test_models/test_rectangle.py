#!/usr/bin/python3
""" Unittest for rectangle class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class Test_args(unittest.TestCase):
    """ Class for unittest of arguments """

    def setUp(self):
        """ Set up for all methods """
        Base._Base__nb_objects = 0

    def test_no_width(self):
        """ Test for no width """
        with self.assertRaises(TypeError):
            r= Rectangle()

    def test_no_height(self):
        """ Test for no height """
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_no_x(self):
        """ Test for no x """
        r = Rectangle(1, 1)
        self.assertEqual(r.x, 0)

    def test_no_y(self):
        """ Test for no y """
        r = Rectangle(1, 1, 1)
        self.assertEqual(r.y, 0)

    def test_no_id(self):
        """ Test for no id """
        r = Rectangle(1, 1, 1, 1)
        self.assertEqual(r.id, 1)

    def test_id(self):
        """ Test for id """
        r = Rectangle(1, 1, 1, 1, 89)
        self.assertEqual(r.id, 89)

    def test_extraarg(self):
        """ Test for no extra arguments """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1)

    def test_width_positive(self):
        """ Positive Int for Width """
        r = Rectangle(5, 1)
        self.assertEqual(r.width, 5)

    def test_width_negative(self):
        """ Negative Int for Width """
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 1)

    def test_width_zero(self):
        """ Zero Int for Width """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

    def test_width_float(self):
        """ pos float for Width """
        with self.assertRaises(TypeError):
            r = Rectangle(1.0, 1)

    def test_width_float_negative(self):
        """ neg float for Width """
        with self.assertRaises(TypeError):
            r = Rectangle(-1.0, 1)

    def test_width_None(self):
        """ None for Width """
        with self.assertRaises(TypeError):
            r = Rectangle(None, 1)

    def test_width_Str(self):
        """ String for Width """
        with self.assertRaises(TypeError):
            r = Rectangle("1", 1)

    def test_width_list(self):
        """ List for Width """
        with self.assertRaises(TypeError):
            r = Rectangle([1], 1)

    def test_width_tuple(self):
        """ Tuple for Width """
        with self.assertRaises(TypeError):
            r = Rectangle((1, ), 1)

    def test_width_set(self):
        """ Set for Width """
        with self.assertRaises(TypeError):
            r = Rectangle({1}, 1)

    def test_height_positive(self):
        """ Positive Int for height """
        r = Rectangle(1, 5)
        self.assertEqual(r.height, 5)

    def test_height_negative(self):
        """ Negative Int for height """
        with self.assertRaises(ValueError):
            r = Rectangle(1, -5)

    def test_height_zero(self):
        """ Zero Int for height """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_height_float(self):
        """ pos float for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1.0)

    def test_height_float_negative(self):
        """ neg float for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, -1.0)

    def test_height_None(self):
        """ None for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, None)

    def test_height_string(self):
        """ String for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, "1")

    def test_height_list(self):
        """ List for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, [1])

    def test_height_tuple(self):
        """ Tuple for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, (1, ))

    def test_height_set(self):
        """ Set for height """
        with self.assertRaises(TypeError):
            r = Rectangle(1, {1})

    def test_x_positive(self):
        """ Positive Int for x """
        r = Rectangle(1, 1, 5)
        self.assertEqual(r.x, 5)

    def test_x_negative(self):
        """ Negative Int for x """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, -5)

    def test_x_zero(self):
        """ Zero Int for x """
        r = Rectangle(1, 1, 0)
        self.assertEqual(r.x, 0)

    def test_x_float(self):
        """ pos float for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1.0)

    def test_x_float_negative(self):
        """ neg float for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, -1.0)

    def test_x_None(self):
        """ None for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, None)

    def test_x_string(self):
        """ String for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, "1")

    def test_x_list(self):
        """ List for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, [1])

    def test_x_tuple(self):
        """ Tuple for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, (1, ))

    def test_x_set(self):
        """ Set for x """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, {1})

    def test_y_positive(self):
        """ Positive Int for y """
        r = Rectangle(1, 1, 1, 5)
        self.assertEqual(r.y, 5)

    def test_y_negative(self):
        """ Negative Int for y """
        with self.assertRaises(ValueError):
            r = Rectangle(1, 1, 1, -5)

    def test_y_zero(self):
        """ Zero Int for y """
        r = Rectangle(1, 1, 1, 0)
        self.assertEqual(r.y, 0)

    def test_y_float(self):
        """ positive float for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1.0)

    def test_y_float_negative(self):
        """ negative float for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, -1.0)

    def test_y_None(self):
        """ None for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, None)

    def test_y_string(self):
        """ Str for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, "1")

    def test_y_list(self):
        """ List for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, [1])

    def test_y_tuple(self):
        """ Tuple for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, (1, ))

    def test_y_set(self):
        """ Set for y """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, {1})


    def test_area1(self):
        """ test area method"""
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area2(self):
        """ test area method"""
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)

    def test_area3(self):
        """ test area method"""
        r = Rectangle(3, 4, 1, 1, 1)
        self.assertEqual(r.area(), 12)

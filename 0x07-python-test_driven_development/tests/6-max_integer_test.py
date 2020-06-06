#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_negative_charge(self):
        l  = [-12, -35, -87, -3]
        self.assertEqual(max_integer(l), -3)

    def test_alone(self):
        l  = [3]
        self.assertEqual(max_integer(l), 3)

    def test_max_empty(self):
        """ Test when an empty list function is passed """
        self.assertEqual(max_integer([]), None)

    def test_matrix(self):
        """ Test when a matrix  dictionary is passed """
        self.assertEqual(max_integer([[2, 4], [4, 7]]), [4, 7])

    def test_repeated_int(self):
        """ Test when a single int is passed as list """
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_string(self):
        l = "holberton"
        self.assertEqual(max_integer(l), 't')

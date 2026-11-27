#!/usr/bin/python3
"""
Unittest module for models/rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_id(self):
        """Test ID assignment for Rectangle instances."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    def test_getters_setters(self):
        """Test getter and setter properties."""
        r = Rectangle(5, 10, 1, 2, 99)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

        r.width = 20
        r.height = 30
        r.x = 4
        r.y = 5
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)


if __name__ == "__main__":
    unittest.main()

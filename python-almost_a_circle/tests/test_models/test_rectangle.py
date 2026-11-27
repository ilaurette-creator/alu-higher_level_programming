#!/usr/bin/python3
"""
Unittest module for models/rectangle.py
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_types(self):
        """Test non-integer types for width, height, x, and y."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "4")

    def test_values(self):
        """Test invalid integer values (<= 0 for width/height, < 0 for x/y)."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test area method calculation."""
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display(self):
        """Test display output with #."""
        r = Rectangle(2, 3)
        captured = io.StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n##\n")


if __name__ == "__main__":
    unittest.main()

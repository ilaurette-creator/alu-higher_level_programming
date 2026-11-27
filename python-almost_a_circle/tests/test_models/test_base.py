#!/usr/bin/python3
"""
Unittest module for models/base.py
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_auto_id(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """Test assigning a custom ID."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_mixed_id(self):
        """Test mixing automatic and custom IDs."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 2)

    def test_negative_id(self):
        """Test passing a negative integer as custom ID."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_string_id(self):
        """Test passing a string as custom ID."""
        b = Base("hello")
        self.assertEqual(b.id, "hello")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""
Unittest module for models/base.py
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up created JSON files after each test."""
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            if os.path.exists(filename):
                os.remove(filename)

    def test_auto_id(self):
        """Test automatic ID incrementation."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test custom ID assignment."""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_to_json_string(self):
        """Test to_json_string method."""
        d = [{'id': 1, 'width': 2, 'height': 3}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"id": 1, "width": 2, "height": 3}]')
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_to_file(self):
        """Test save_to_file class method."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = f.read()
        self.assertIn('"id": 1', content)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_from_json_string(self):
        """Test from_json_string static method."""
        json_str = '[{"id": 89, "width": 10, "height": 4}]'
        res = Base.from_json_string(json_str)
        self.assertEqual(res, [{'id': 89, 'width': 10, 'height': 4}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_create(self):
        """Test create class method."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)

        s1 = Square(5, 1, 3, 99)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)

    def test_load_from_file(self):
        """Test load_from_file class method."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertEqual(str(out[0]), str(r1))
        self.assertEqual(str(out[1]), str(r2))


if __name__ == "__main__":
    unittest.main()

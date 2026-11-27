#!/usr/bin/python3
"""
Unittest module for models/square.py
"""
import io
import os
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Clean up created Square.json file after tests."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_square_instantiation(self):
        """Test Square instantiation and default values."""
        s1 = Square(5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 2, 3, 12)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 12)

    def test_square_negative_size(self):
        """Test Square(-1) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)

    def test_square_zero_size(self):
        """Test Square(0) raises ValueError."""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_square_size_getter_setter(self):
        """Test size getter and setter validation."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0

    def test_square_x_y_validation(self):
        """Test x and y validation for Square."""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 2, "3")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(5, 2, -3)

    def test_square_str(self):
        """Test __str__ representation for Square."""
        s = Square(5, 1, 3, 99)
        self.assertEqual(str(s), "[Square] (99) 1/3 - 5")

    def test_square_area(self):
        """Test inherited area method on Square."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_square_display(self):
        """Test inherited display method on Square."""
        s = Square(2, 2, 1)
        captured = io.StringIO()
        sys.stdout = captured
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n  ##\n  ##\n")

    def test_square_update_args(self):
        """Test update method with positional arguments (*args)."""
        s = Square(5, 0, 0, 1)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(10, 2)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 2")
        s.update(10, 2, 3)
        self.assertEqual(str(s), "[Square] (10) 3/0 - 2")
        s.update(10, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (10) 3/4 - 2")

    def test_square_update_kwargs(self):
        """Test update method with keyword arguments (**kwargs)."""
        s = Square(5, 0, 0, 1)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(id=89, size=3, x=4, y=5)
        self.assertEqual(str(s), "[Square] (89) 4/5 - 3")

    def test_to_dictionary(self):
        """Test to_dictionary method for Square."""
        s = Square(10, 2, 1, 1)
        s_dict = s.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s_dict, expected)

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None)."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test Square.save_to_file([])."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_square(self):
        """Test Square.save_to_file([Square(1)])."""
        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(
                f.read(),
                '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
            )

    def test_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_exists(self):
        """Test Square.load_from_file() when file exists."""
        s1 = Square(5, 1, 2, 10)
        s2 = Square(7, 0, 0, 11)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(len(output), 2)
        self.assertEqual(str(output), str(s1))
        self.assertEqual(str(output), str(s2))


if __name__ == "__main__":
    unittest.main()

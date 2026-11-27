#!/usr/bin/python3
"""
Module square
Defines the Square class that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (int, optional): Identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size.
        Assigns width and height in order with the same value.
        Validation is inherited from Rectangle's width setter.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """
        Assigns attributes to Square instance:
        - *args: 1st=id, 2nd=size, 3rd=x, 4th=y
        - **kwargs: key/value pairs (skipped if *args exists and non-empty)
        """
        if args and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

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

    def __str__(self):
        """
        Returns the string representation of the Square instance.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

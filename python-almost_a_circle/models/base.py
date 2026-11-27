#!/usr/bin/python3
"""
Module base
Defines the Base class for all other classes in this project.
"""


class Base:
    """
    Base class to manage id attribute in all future classes.

    Attributes:
        __nb_objects (int): Private class attribute tracking instance count.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): Identifier for the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

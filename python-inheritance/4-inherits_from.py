#!/usr/bin/python3
"""Defines an inherited class check function."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a subclass of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against.

    Returns:
        bool: True if obj is an instance of a subclass, else False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """A subclass of list with custom printing behavior."""

    def print_sorted(self):
        """Print the list in ascending sorted order without modifying it."""
        print(sorted(self))

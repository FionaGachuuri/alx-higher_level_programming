#!/usr/bin/python3
"""Module that defines a class MyList
that inherits fom list."""


class MyList(list):
    """Custom class that inherits the
    built-in list class."""
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))

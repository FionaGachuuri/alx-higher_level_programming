#!/usr/bin/python3
"""Module that defines a class BaseGeometry with a method area
that raises an exception when called."""


class BaseGeometry:
    """A class representing basic geometry."""
    def area(self):
        """Raises an Exception with the message area()
        is not implemented."""
        raise Exception("area() is not implemented")

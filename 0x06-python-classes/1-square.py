#!/usr/bin/python3
"""
This module defines a square class with a private attribute."""


class Square:
    """
    A class  that defines a square by it's size.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self,size):
        """
        Initializes the square with a private size attribute.
        Args:
            size (int): The square's size.
        """
        self.__size = size

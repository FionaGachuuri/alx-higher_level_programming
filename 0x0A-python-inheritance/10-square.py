#!/usr/bin/python3
"""Module that defines a class Square that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square, inheriting from Rectangle."""

    def __init__(self, size):
        """
        Initialize a new square instance.

        Args:
            size (int): The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Rectangle] {self.__size}/{self.__size}"

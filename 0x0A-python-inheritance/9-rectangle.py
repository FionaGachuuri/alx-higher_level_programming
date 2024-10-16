#!/usr/bin/python3
"""A module that writes a class Rectangle that inherits
from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    "Class representing a rectangle, inheriting from BaseGeometry."""

    def __init__(self, width, height):
        """Initializing a new rectangle instance."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculating the area of the rectangle(width *haight)."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"

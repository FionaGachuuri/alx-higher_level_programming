#!/usr/bin/python3
"""A module that defines a class Rectangle that inherits
from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class represents a rectangle using BaseGeometry"""
    def __init__(self, width, height):
        """Initializing an new rectangle."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of a Rectangle object"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string

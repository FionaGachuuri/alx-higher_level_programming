#!/usr/bin/python3
"""
This is '2-rectangle' modulei that computes
the perimeter and area of a rectangle.
"""


class Rectangle():
    """representing a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """find and return the rectangle's area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """find and return rectangle's perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)

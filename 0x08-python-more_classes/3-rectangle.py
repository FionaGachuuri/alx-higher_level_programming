#!/usr/bin/python3
"""
This is 3-rectangle module that defines a rectangle.
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
        """find and return the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """find and return the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        s = ""
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                s += "#"
            if (i+1) != self.__height:
                s += "\n"
        return s

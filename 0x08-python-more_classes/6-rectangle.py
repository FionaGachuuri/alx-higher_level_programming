#!/usr/bin/python3
"""
This is '6-rectangle' module.
Defines a Rectangle class with various methods for calculating area,perimeter
and controlling instances, as well as special string representations.
"""


class Rectangle():
    """representing a rectangle with width, height and additional methods"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        """print and return the rectangle area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """print and return the rectangle perimeter"""
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

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

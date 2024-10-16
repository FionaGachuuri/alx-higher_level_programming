#!/usr/bin/python3
"""Module that defines a class BaseGeometry with methods to
calculate area and validate integer values."""


class BaseGeometry:
    """A class representing basic geometry."""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as a positive integer.

        Args:
            name (str): The name of the variable (for error messages).
            value: The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

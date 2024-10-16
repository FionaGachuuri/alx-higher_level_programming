#!/usr/bin/python3
"""Module that defines a function to add a new attribute to an object."""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to which the attribute is to be added.
        attr (str): The name of the attribute.
        value: The value of the attribute to be added.

    Raises:
        TypeError: If the attribute can't be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)

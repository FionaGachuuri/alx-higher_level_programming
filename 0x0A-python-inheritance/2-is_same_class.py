#!/usr/bin/python3
"""Module that defines a function that checks if an object
is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Checks if obj is an exact instance of a_class."""
    return type(obj) is a_class

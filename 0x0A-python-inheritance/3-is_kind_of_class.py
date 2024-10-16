#!/usr/bin/python3
"""Module that defines a function that checks if an object
is an instance of a class or its subclasses."""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of a_class or a
    subclass of a_class."""
    return isinstance(obj, a_class)

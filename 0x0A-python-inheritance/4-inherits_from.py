#!/usr/bin/python3
"""Module that defines a function that checks if an object
is an instance of a class that inherited from a specified
class whether directly or indirectly."""


def inherits_from(obj, a_class):
    """ Checks if obj is an instance of
    a class that inherited from a class.

    Arguments:
        obj: object to be checked.
        a_class: class to be checked against.

    Returns:
        True if obj is an instance of a class that
        inherited from a_class, otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""Module that defines function that returns
the JSON representation of an object (string)."""


def to_json_string(my_obj):
    """Returns the JSON representation of an object."""
    return __import__('json').dumps(my_obj)

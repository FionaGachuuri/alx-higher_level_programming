#!/usr/bin/python3
"""Module that defines a function returns a python
data structure represented  by a JSON string."""


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string"""
    return __import__('json').loads(my_str)

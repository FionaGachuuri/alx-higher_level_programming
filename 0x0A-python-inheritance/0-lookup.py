#!/usr/bin/python3
"""Module that returns list of an object's
attributes and methods."""


def lookup(obj):
    """Returns a list of available
    attributes and methods of an object."""
    return dir(obj)

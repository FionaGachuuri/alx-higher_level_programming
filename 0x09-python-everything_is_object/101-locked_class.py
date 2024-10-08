#!/usr/bin/python3
"""This module defines a class LockedClass"""


class LockedClass:
    """
    It doesn't allow the user to dynamically
    create new instance attributes,
    only if the new instance attribute is called first_name.

    Attributes:
        first_name (str): first name of something.
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates  the new instances of Locked Class."""

        self.first_name = "first_name"

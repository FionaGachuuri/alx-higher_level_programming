#!/usr/bin/python3
"""Module that defines a class Base
that manages id attribute."""


class Base:
    """Base class that manages 'id'
    attribute of future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class.
        Args:
            id (int, optional): The id of the instance.
            If none, an id is automatically asssigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

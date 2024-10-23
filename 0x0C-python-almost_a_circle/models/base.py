#!/usr/bin/python3
"""Module that defines a class Base
that manages id attribute."""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list):
            A list of dictionaries to convert to JSON.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances that inherit from Base,
            ie Rectangle or Square.
        """
        filename = cls.__name__ + ".json"
        list_dicts = ([obj.to_dictionary() for obj in list_objs]
                      if list_objs else [])
        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_string)

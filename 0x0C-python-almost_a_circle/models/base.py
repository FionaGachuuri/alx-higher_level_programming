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
        
    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: If json_string is None or empty, returns an empty list,
            otherwise returns the list represented by the JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)   

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs if hasattr(obj, 'to_dictionary')]
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

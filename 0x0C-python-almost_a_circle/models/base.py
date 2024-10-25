#!/usr/bin/python3
"""Module that defines a class Base
that manages id attribute."""

import csv
import json
from os import path


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
        list_dicts = [
            obj.to_dictionary()
            for obj in list_objs
            if hasattr(obj, 'to_dictionary')
            ]
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set.

        Args:
            **dictionary: Key-value pairs
            representing attributes of the instance.
        Returns:
            An instance of the class with attributes set.
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load list of instances from a JSON file.

        Returns:
            list: List of instances created from the JSON file data.
        """
        filename = f"{cls.__name__}.json"
        if not path.isfile(filename):
            return []
        with open(filename, 'r') as file:
            json_string = file.read()
            list_dicts = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save list of instances to a CSV file.

        Args:
            list_objs (list): List of instances to save.
        """
        filename = f"{cls.__name__}.csv"
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Load list of instances from a CSV file.

        Returns:
            list: List of instances created from CSV file data.
        """
        filename = f"{cls.__name__}.csv"
        
        # Check if the file exists
        if not path.isfile(filename):
            return []
        
        # Read from the file and load instances
        instances = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            
            for row in reader:
                if cls.__name__ == "Rectangle":
                    id_, width, height, x, y = map(int, row)
                    obj = cls(width, height, x, y, id_)
                elif cls.__name__ == "Square":
                    id_, size, x, y = map(int, row)
                    obj = cls(size, x, y, id_)
                instances.append(obj)
        
        return instances
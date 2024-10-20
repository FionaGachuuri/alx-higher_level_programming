#!/usr/bin/python3
"""Module that defines a function that writes an
object to a text file using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
    using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(__import__('json').dumps(my_obj))

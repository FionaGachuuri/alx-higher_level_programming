#!/usr/bin/python3
"""Module that defines a function
that creates an Object from a “JSON file”."""


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename, 'r', encoding='utf-8') as file:
        return __import__('json').load(file)

#!/usr/bin/python3
"""Unittest for Base class."""

import unittest
from models.base import Base
from models.rectangle import Rectangle
import os
import json


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Resets the private class attribute between tests."""
        Base._Base__nb_objects = 0

    def test_id_auto_increment(self):
        """Test automatic id assignment and increment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_custom(self):
        """Test custom id assignment."""
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_to_json_string_none(self):
        """Test JSON string output when input is None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test JSON string output when input is an empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_content(self):
        """Test JSON string output with valid list of dictionaries."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_str = Base.to_json_string(list_dicts)
        self.assertEqual(json_str, json.dumps(list_dicts))

    def test_save_to_file_none(self):
        """Test save_to_file with None input, should create an empty file."""
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list."""
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_content(self):
        """Test save_to_file with actual list of Base instances."""
        b1 = Rectangle(1, 2, id=1)  # Replace with appropriate attributes
        b2 = Rectangle(3, 4, id=2)
        Base.save_to_file([b1, b2])

        with open("Rectangle.json", "r") as f:
            content = f.read()
            expected_content = json.dumps([b1.to_dictionary(), b2.to_dictionary()])
            self.assertEqual(content, expected_content)

    def tearDown(self):
        """Cleanup created files after each test."""
        if os.path.exists("Base.json"):
            os.remove("Base.json")


if __name__ == "__main__":
    unittest.main()

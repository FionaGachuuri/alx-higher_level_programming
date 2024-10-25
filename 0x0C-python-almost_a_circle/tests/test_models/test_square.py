#!/usr/bin/python3
"""Unit test for the Square class."""

import unittest
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Set up for testing, reset Base class id count."""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Test initialization of the Square instance."""
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.height, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertIsNotNone(sq.id)

    def test_size_setter(self):
        """Test setting the size attribute."""
        sq = Square(5)
        sq.size = 10
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)

        with self.assertRaises(TypeError):
            sq.size = "10"
        with self.assertRaises(ValueError):
            sq.size = -5

    def test_update_args(self):
        """Test update method with *args."""
        sq = Square(5)
        sq.update(10, 7, 2, 3)
        self.assertEqual(sq.id, 10)
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        sq = Square(5)
        sq.update(id=15, size=8, x=4, y=5)
        self.assertEqual(sq.id, 15)
        self.assertEqual(sq.size, 8)
        self.assertEqual(sq.x, 4)
        self.assertEqual(sq.y, 5)

    def test_to_dictionary(self):
        """Test dictionary representation of a Square."""
        sq = Square(5, 1, 2, 10)
        sq_dict = sq.to_dictionary()
        expected_dict = {'id': 10, 'size': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(sq_dict, expected_dict)

    def test_str_method(self):
        """Test __str__ method output."""
        sq = Square(4, 2, 3, 25)
        self.assertEqual(str(sq), "[Square] (25) 2/3 - 4")

if __name__ == "__main__":
    unittest.main()


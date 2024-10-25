#!/usr/bin/python3
"""Unit tests for the Rectangle class."""

import io
from unittest import mock

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Defines unit tests for the Rectangle class."""

    def setUp(self):
        """Set up for testing each method."""
        self.rect1 = Rectangle(3, 4, 1, 2, 99)

    def test_initialization(self):
        """Test initialization and attribute assignment."""
        rect = Rectangle(10, 2, 1, 3, 101)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 101)

    def test_width_height_validation(self):
        """Test width and height for correct and incorrect values."""
        with self.assertRaises(TypeError):
            Rectangle("width", 10)
        with self.assertRaises(ValueError):
            Rectangle(-5, 10)
        with self.assertRaises(TypeError):
            Rectangle(10, "height")
        with self.assertRaises(ValueError):
            Rectangle(10, -5)

    def test_x_y_validation(self):
        """Test x and y for correct and incorrect values."""
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "x", 3)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 3)
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 3, "y")
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 3, -1)

    def test_area(self):
        """Test the area method."""
        self.assertEqual(self.rect1.area(), 12)
        rect = Rectangle(10, 2)
        self.assertEqual(rect.area(), 20)

    def test_display(self):
        """Test the display method's output format."""
        rect = Rectangle(2, 2, 2, 1)
        expected_output = "\n  ##\n  ##\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test the __str__ method."""
        self.assertEqual(str(self.rect1), "[Rectangle] (99) 1/2 - 3/4")

    def test_update_args(self):
        """Test update method with *args."""
        self.rect1.update(89, 5, 7, 8, 9)
        self.assertEqual(self.rect1.id, 89)
        self.assertEqual(self.rect1.width, 5)
        self.assertEqual(self.rect1.height, 7)
        self.assertEqual(self.rect1.x, 8)
        self.assertEqual(self.rect1.y, 9)

    def test_update_kwargs(self):
        """Test update method with **kwargs."""
        self.rect1.update(width=10, height=12, x=1, y=3)
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 12)
        self.assertEqual(self.rect1.x, 1)
        self.assertEqual(self.rect1.y, 3)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        expected_dict = {'id': 99, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(self.rect1.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
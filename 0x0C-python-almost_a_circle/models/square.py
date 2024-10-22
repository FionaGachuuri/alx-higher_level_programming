#!/usr/bin/python3
"""Module that defines a Square class that inherits from Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Reps a square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square; width and height.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The id of the square inherited from Rectangle.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter function  for the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size of the square, assigns to width and height.

        Args:
            value(int): The size to set for both width and height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

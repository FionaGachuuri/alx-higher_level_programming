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

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

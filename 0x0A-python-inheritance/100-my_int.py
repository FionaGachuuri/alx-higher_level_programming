#!/usr/bin/python3
"""Module that defines a class MyInt that inherits from int."""


class MyInt(int):
    """A rebel integer class that inverts equality operators."""

    def __eq__(self, other):
        """Inverted equality comparison."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted non-equality comparison."""
        return super().__eq__(other)

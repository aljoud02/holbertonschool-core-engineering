#!/usr/bin/env python3
"""
This module defines an extended Square class with custom string format.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a complete square shape with individual descriptions.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance based on size constraints.

        Args:
            size (int): The single size measurement for all sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Provides a custom human-readable description for the square instance.

        Returns:
            str: Description containing the size formatting.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

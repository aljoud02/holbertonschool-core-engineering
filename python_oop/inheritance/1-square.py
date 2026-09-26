#!/usr/bin/env python3
"""
This module defines a basic Square class inheriting from Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a specialized square shape inheriting from Rectangle layout.
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

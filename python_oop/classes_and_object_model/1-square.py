#!/usr/bin/env python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Defines a square template with size encapsulation.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square sides.
        """
        self.__size = size

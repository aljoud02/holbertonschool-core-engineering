#!/usr/bin/env python3
"""
This module defines an extended Rectangle class with area and string methods.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a complete rectangle shape with computations and formats.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance with dimensions validation.

        Args:
            width (int): The width dimension.
            height (int): The height dimension.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the structural area of the rectangle.

        Returns:
            int: The calculated area size.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Provides a custom human-readable string representation of the object.

        Returns:
            str: Description containing the dimensions formatting.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

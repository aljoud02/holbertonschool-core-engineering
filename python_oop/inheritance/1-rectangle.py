#!/usr/bin/env python3
"""
This module defines a basic Rectangle class inheriting from BaseGeometry.
"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape built upon foundational geometry behaviors.
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

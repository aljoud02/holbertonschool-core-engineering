#!/usr/bin/env python3
"""
This module defines a foundational class for geometric shapes.
"""


class BaseGeometry:
    """
    A foundational class representing geometry blueprints and validations.
    """

    def area(self):
        """
        Calculates the area of the shape.

        Raises:
            Exception: Indicates the calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value represents a valid positive integer.

        Args:
            name (str): The name identifier associated with the value.
            value: The data to check.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

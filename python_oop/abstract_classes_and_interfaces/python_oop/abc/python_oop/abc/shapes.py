#!/usr/bin/env python3
"""
This module defines abstract geometry shapes and demonstrates duck typing.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class representing a generic geometric shape contract.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to compute the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to compute the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Concrete subclass representing a circle geometry layout.
    """

    def __init__(self, radius):
        """
        Initializes a new Circle instance.

        Args:
            radius (float): The radius dimension.
        """
        self.__radius = radius

    def area(self):
        """
        Computes the area of the circle.

        Returns:
            float: The calculated area size.
        """
        return math.pi * (self.__radius ** 2)

    def perimeter(self):
        """
        Computes the perimeter of the circle.

        Returns:
            float: The calculated perimeter size.
        """
        return 2 * math.pi * self.__radius


class Rectangle(Shape):
    """
    Concrete subclass representing a rectangle geometry layout.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle instance.

        Args:
            width (float): The width dimension.
            height (float): The height dimension.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            float: The calculated area size.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
            float: The calculated perimeter size.
        """
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    """
    Standalone function that prints shape information using duck typing.

    Args:
        shape: An object satisfying the Shape method contract.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))

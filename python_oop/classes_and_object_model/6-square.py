#!/usr/bin/env python3
"""
This module defines a Square class with size and position properties,
including custom string representation capabilities.
"""


class Square:
    """
    Defines a square template with encapsulation, printing, and string methods.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square sides. Default is 0.
            position (tuple): The position of the square in spaces.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the private size attribute with full input validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the private position attribute.

        Returns:
            tuple: A tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the private position attribute with type and value validation.

        Args:
            value (tuple): A tuple containing exactly two positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character # to stdout.
        Uses position to prepend spaces and newlines.
        """
        if self.__size == 0:
            print("")
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Defines the informal string representation of the Square instance.

        Returns:
            str: The square represented by # characters with position layout.
        """
        if self.__size == 0:
            return ""

        res = "\n" * self.__position[1]
        for i in range(self.__size):
            res += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                res += "\n"
        return res

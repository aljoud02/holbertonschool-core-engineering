#!/usr/bin/env python3
"""
This module defines an abstract Animal class and its concrete subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract class representing a generic animal entity.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses to return
        the respective animal sound.
        """
        pass


class Dog(Animal):
    """
    Concrete subclass representing a dog entity.
    """

    def sound(self):
        """
        Implements the sound method for a dog.

        Returns:
            str: The sound of a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete subclass representing a cat entity.
    """

    def sound(self):
        """
        Implements the sound method for a cat.

        Returns:
            str: The sound of a cat.
        """
        return "Meow"

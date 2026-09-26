#!/usr/bin/env python3
"""
This module explores multiple inheritance behaviors and method resolution.
"""


class Fish:
    """
    Defines a base class representing fish entities and aquatic behaviors.
    """

    def swim(self):
        """
        Prints a generic fish swimming phrase.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Prints a generic fish environmental habitat location.
        """
        print("The fish lives in water")


class Bird:
    """
    Defines a base class representing bird entities and aerial behaviors.
    """

    def fly(self):
        """
        Prints a generic bird flying phrase.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Prints a generic bird environmental habitat location.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Subclass combining fish and bird capabilities through multiple inheritance.
    """

    def swim(self):
        """
        Overrides the swim behavior for a specialized flying fish.
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        Overrides the fly behavior for a specialized flying fish.
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        Overrides the habitat layout for a specialized flying fish.
        """
        print("The flying fish lives both in water and the sky!")

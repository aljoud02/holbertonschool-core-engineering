#!/usr/bin/env python3
"""
This module demonstrates composition design via isolated mixin modules.
"""


class SwimMixin:
    """
    Provides isolated swimming capabilities for composite structures.
    """

    def swim(self):
        """
        Executes a localized swimming behavioral routine output.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Provides isolated flying capabilities for composite structures.
    """

    def fly(self):
        """
        Executes a localized flying behavioral routine output.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Composite class leveraging mixins to combine dynamic capabilities.
    """

    def roar(self):
        """
        Executes a specialized dragon voice routine output.
        """
        print("The dragon roars!")

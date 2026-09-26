#!/usr/bin/env python3
"""
This module defines a custom subclass that extends the built-in list type.
"""


class VerboseList(list):
    """
    A custom list variant that prints actions when contents are modified.
    """

    def append(self, item):
        """
        Appends an item and prints a notification layout.
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        Extends the sequence and prints a notification layout.
        """
        item_count = len(x)
        super().extend(x)
        print("Extended the list with {} items.".format(item_count))

    def remove(self, item):
        """
        Removes a target item and prints a notification layout.
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Pops an index element and prints a notification layout.
        """
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
        return item

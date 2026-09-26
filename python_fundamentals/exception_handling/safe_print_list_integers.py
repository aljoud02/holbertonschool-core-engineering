#!/usr/bin/env python3
"""
This module provides a function for safely printing integers from a list.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, but only if they are integers.

    Args:
        my_list (list): The list containing elements of any type.
        x (int): The number of elements to access from the list.

    Returns:
        int: The number of integers successfully printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")  # Print the mandatory newline character at the end
    return count

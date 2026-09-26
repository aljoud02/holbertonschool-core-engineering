#!/usr/bin/env python3
"""
This module provides a function for safely printing elements from a list.
"""


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list on the same line followed by a new line.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break
    print("")  # Print the mandatory newline character at the end
    return count

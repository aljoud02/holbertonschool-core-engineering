#!/usr/bin/env python3
"""
This module provides a function for safely printing an integer.
"""


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        bool: True if value has been correctly printed, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False

#!/usr/bin/env python3
"""
This module provides a function for safely dividing two integers.
"""


def safe_print_division(a, b):
    """
    Divides two integers and prints the result inside a finally block.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The result of the division, or None if an error occurs.
    """
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError, ValueError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return result


#!/usr/bin/env python3
"""
This module provides a function that raises a NameError with a message.
"""


def raise_exception_msg(message=""):
    """
    Raises a NameError with a custom message.

    Args:
        message (str): The message to include in the NameError.
    """
    raise NameError(message)

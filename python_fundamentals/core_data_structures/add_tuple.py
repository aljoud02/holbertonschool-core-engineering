#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Adds the first two elements of two tuples and returns a new tuple."""
    # Extract elements for tuple_a or use 0 if missing
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0

    # Extract elements for tuple_b or use 0 if missing
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Return the new tuple with exactly two integers
    return (a1 + b1, a2 + b2)

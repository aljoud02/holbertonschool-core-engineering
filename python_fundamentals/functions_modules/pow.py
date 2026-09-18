#!/usr/bin/env python3
# Function to compute a raised to the power of b using a loop


def pow(a, b):
    result = 1
    for _ in range(b):
        result *= a
    return result

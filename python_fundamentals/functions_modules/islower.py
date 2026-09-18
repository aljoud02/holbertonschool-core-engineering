#!/usr/bin/env python3
# Function to check if a character is lowercase using ASCII logic


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

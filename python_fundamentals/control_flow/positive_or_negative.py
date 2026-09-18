#!/usr/bin/env python3
# Script to check if a random number is positive, zero, or negative
number = __import__('random').randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")

#!/usr/bin/env python3
# Script to print the last digit of a random number with its properties
number = __import__('random').randint(-10000, 10000)

if number < 0:
    last_digit = (-number % 10) * -1
else:
    last_digit = number % 10

output_base = f"Last digit of {number} is {last_digit}"

if last_digit > 5:
    print(f"{output_base} and is greater than 5")
elif last_digit == 0:
    print(f"{output_base} and is 0")
else:
    print(f"{output_base} and is less than 6 and not 0")


#!/usr/bin/env python3
# Function that prints and returns the absolute last digit of a number


def print_last_digit(number):
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit

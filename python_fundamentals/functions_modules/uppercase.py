#!/usr/bin/env python3
# Function to print a string in uppercase using ASCII shifts


def uppercase(str):
    result = ""
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))

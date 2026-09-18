#!/usr/bin/env python3
# Script to print numbers from 00 to 99 with custom formatting
for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else:
        print("{:02d}".format(i))

#!/usr/bin/env python3
# Script to print numbers from 00 to 99 with proper indentation
for i in range(100):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")

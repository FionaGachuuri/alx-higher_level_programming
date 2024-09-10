#!/usr/bin/python3

def uppercase(s):
    """Print the string s in uppercase."""
    for char in s:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
        print(char, end="")
    print()

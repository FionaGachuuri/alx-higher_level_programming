#!/usr/bin/python3

def uppercase(str):
    """Prints the given string in uppercase."""
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - ord('a') + ord('A'))
        print(char, end="")
    print()

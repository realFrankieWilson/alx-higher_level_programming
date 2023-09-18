#!/usr/bin/python3
# 1-write_file.py
""" Write a function that writes a string to a text file (UTF8) and returns the
number of characters written """


def write_file(filename="", text=""):
    """
    Args:
        filename filename
        text to be written into filename
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

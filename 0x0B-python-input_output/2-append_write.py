#!/usr/bin/python3
# 2-append_write.py
""" A function that appends a string at the end of a text file (UTF8)
    Returns the number of characters added.
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

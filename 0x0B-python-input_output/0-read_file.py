#!/usr/bin/python3
# 0-read_file.py
""" A function that reads file to stdoutput """


def read_file(filename=""):
    """
    Args:
        filename name of the file to be read
    """
    with open(filename, encoding='utf-8') as res:
        x = res.read()
    print(x)

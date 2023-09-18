#!/usr/bin/python3
# 0-read_file.py
""" A function that reads file to stdoutput """


def read_file(filename=""):
    """ filename name of the file to be read """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')

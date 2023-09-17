#!/usr/bin/python3
# 2-is_same_class.py
""" A function that check for the type of an object """


def is_same_class(obj, a_class):
    """ checks if object is an int or not """
    if type(obj) is a_class:
        return True
    return False

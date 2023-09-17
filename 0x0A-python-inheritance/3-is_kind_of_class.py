#!/usr/bin/python3
# 3-is_kind_of_class.py
"""
A Function that returns True if the object is an istance or if the object
is an instance that returns it
"""


def is_kind_of_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    return False

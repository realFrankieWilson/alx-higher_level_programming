#!/usr/bin/python3
# 3-is_kind_of_class.py
"""
A Function that returns True if the object is an istance or if the object
is an instance that returns it
"""


def is_kind_of_class(obj, a_class):
    """ Args:
        obj: The object to be compared with
        a_class: The class to compare with the object
    Returns:
        True-> if the object is an int or inherieted from the specified class
        Otherwise False is returned
    """
    return (isinstance(obj, a_class))

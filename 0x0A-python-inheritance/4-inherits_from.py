#!/usr/bin/python3
# 4-inherits_from.py
"""
A function that returns True if the object is an istance of a class that
Inherited (directly or indirectly) from the specified class: otherwise False.
"""


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of a class that inherited from the
    specified class, Otherwise False is returned
    """
    if isinstance(obj, a_class) and issubclass(a_class, obj.__class__)\
            is False:
        return True
    return False

#!/usr/bin/python3
# 101-add_attribute.py
""" Defines a function that adds attributes to objects. """


def add_attribute(obj, att, value):
    """ Add a new attribute to an object if possible.
    Args: obj : the object to add attribute to.
        att: The name of the attribute to add to obj.
        value: The value att.
    Raise:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)

#!/usr/bin/python3
"""
The module is about adding two integers
The 0-add_integer module supplies one function, add_integer(a, b).
and it only takes in integer or float
"""


def add_integer(a, b=98):
    """
    Adds a to b, (both integers ) just checking
    Args:
        a -> is an int;
        b -> is an int;
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(a, int) and not isinstance(a, float))):

        raise TypeError("b must be an integer")

    return (int(a) + int(b))

#!/usr/bin/python3
"""
The module is about adding two integers
The 0-add_integer module supplies one function, add_integer(a, b).
and it only takes in integer or float
"""


def add_integer(a, b=98):
    """ Return sum of two integers or floats

    Args:
        a -> is an int;
        b -> is an int;

    Returns:
        sum of a and b

    Raises:
        TypeError: if the arguments are not int or float

    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b

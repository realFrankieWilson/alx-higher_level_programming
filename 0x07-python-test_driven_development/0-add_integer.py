#!/usr/bin/python3
"""
The module is about adding two integers
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b=98):
    """ Return sum of two integers or floats


    Args:
        a is the first argument
        b is the second argumet

    Returns:
        sum of a and b


    Raises:
        TypeError: if the arguments are not int or float
    Rasise:
        TypeError: if the arguments are not float or int


    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

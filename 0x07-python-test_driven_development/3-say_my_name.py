#!/usr/bin/python3
# 3-say_my_name.py
"""
This function prints my name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name -> Argument of the Person's Frist name
        last_name -> Argument of the Person's Last name
    Raise:
        TypeError -> If first and last name are not string.
    """

    # Error messages to display
    f_name_error_msg = "first_name must be a string"
    l_name_error_msg = "last_name must be a string"

    # Error messages condition:
    if ((not isinstance(first_name, str))):
        raise TypeError(f_name_error_msg)

    # check for the last name:
    if ((not isinstance(last_name, str))):
        raise TypeError(l_name_error_msg)

    print("My name is {} {}".format(first_name, last_name))

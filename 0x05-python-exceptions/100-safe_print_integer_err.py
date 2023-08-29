#!/usr/bin/python3
from sys import exc_info, stderr

def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(exc_infor()[1]), file=stderr)
        return False

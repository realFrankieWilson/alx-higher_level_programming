#!/usr/bin/python3
# 8-class_to_json.py
""" Returns the dictionary description with simple data structure (list,
dictionary, string, integer and boolean) for json serialization of an object"""


def class_to_json(obj):
    """ obj is an istance of a class """
    return obj.__dict__

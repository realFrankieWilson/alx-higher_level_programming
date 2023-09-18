#!/usr/bin/python3
# 3-to_json_string.py
""" A Function that returns the JSON representation of an object(string): """
import json


def to_json_string(my_obj):
    """ Returns a json file version of an object """
    return json.dumps(my_obj)

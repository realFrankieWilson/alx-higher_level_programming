#!/usr/bin/python3
# 4-from_json_string.py
""" A function that returns an object (Python data structure)
    represented by a JSON """
import json


def from_json_string(my_str):
    """ Returning an object represented by JSON str """
    return json.loads(my_str)

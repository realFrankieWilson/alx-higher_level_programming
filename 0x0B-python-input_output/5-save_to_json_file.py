#!/usr/bin/python3
# 5-save_to_json_file.py
""" Writes an object to a txt file, using a JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ Returns the Json representation of my_obj """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))

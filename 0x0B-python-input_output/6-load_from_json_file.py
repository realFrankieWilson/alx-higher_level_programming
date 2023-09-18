#!/usr/bin/python3
# 6-load_from_jeson_file.py
""" Creates an Object from a "JSON file": """
import json


def load_from_json_file(filename):
    """ Creates a python obj from a json file """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())

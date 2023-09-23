#!/usr/bin/python3
# base.py
""" The base class module """
import json


class Base:
    """
    A base class or parent class
    """

    __nb_objects = 0    # A private class object attribute

    def __init__(self, id=None):    # Class constructor
        """ class initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A static function of a class that returns a json string """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

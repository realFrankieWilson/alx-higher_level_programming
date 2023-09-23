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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class method that writes the JSON string representation of a list
        object
        """
        file_n = '{}.json'.format(cls.__name__)
        if not list_objs:
            list_objs = []

        with open(file_n, 'w') as f:
            f.write(cls.to_json_string(
                [cls.to_dictionary(x) for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of json string representations """

        json_string_lst = []

        if not json_string_lst and not '':
            if type(json_string) is not str:
                raise TypeError('json_string must be a string')
            json_string_lst = json.loads(json_string)

        return json_string_lst

    @classmethod
    def create(cls, **dictionary):
        """
        A dictionary class mehtod that returns an object with all attributes
        already set
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)

        if cls.__name__ == 'Square':
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        file_n = '{}.json'.format(cls.__name__)
        try:
            with open(file_n, 'r') as f:
                file_list = cls.from_json_string(f.read())
                return [cls.create(**ind) for ind in file_list]
        except IOError:
            return []

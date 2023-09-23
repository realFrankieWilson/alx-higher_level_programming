#!/usr/bin/python3
# base.py
""" The base class module """
import json
import csv


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

        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

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
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method aht serializes list objects and save them to a specified file """

        # A TypeError is Rasied in the following cases:
        # 1. If all the instances in the tuple (i, cls) of the
        #       are not the object instances.
        # 2. If List and list objects are not of type list objects or if
        #       list is empty.
        #
        #   Example: TypeError: List object must be a list of instances.

        file_n = '{}.csv'.format(cls.__name__)
        with open(file_n, 'w', newline='') as f:
            if not list_objs:
                f.write('[]')
            else:

                if cls.__name__ == 'Rectangle':
                    fildnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fildnames = ['id', 'size', 'x', 'y']

                write_to = csv.DictWriter(f, fildnames=fildnames)
                for instance in list_objs:
                    write_to.writerow(instance.to_dictionary())



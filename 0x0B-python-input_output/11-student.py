#!/usr/bin/python3
# 11-student.py
""" A class sudent """


class Student:
    """ Rep Student class """

    def __init__(self, first_name, last_name, age):
        """ the initializer of the self """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Gets a dict rep of the Student
        if atts is a list of strings, rep only the attributes included """
        if (type(attrs) is list and all(type(i) is str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Reloads all attributes of a student """
        for a, b in json.items():
            setattr(self, a, b)

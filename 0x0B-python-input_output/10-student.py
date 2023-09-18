#!/usr/bin/python3
# 10-student.py
""" Defines a class based by file 9-student.py """


class Student:
    """ Rep a Student class """

    def __init__(self, first_name, last_name, age):
        """ the init initializer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get a dictionary rep of the student
        if attrs is a list, strings, rep only those attrs included in the list
        """
        if (type(attrs) is list and all(type(i) is str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

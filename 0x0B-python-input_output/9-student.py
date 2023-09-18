#!/usr/bin/python3
# 9-student.py
""" A Student module """


class Student:
    """ Rep a Student class """
    def __init__(self, first_name, last_name, age):
        """ The initializer """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrives a dict representation of a student class """
        return self.__dict__

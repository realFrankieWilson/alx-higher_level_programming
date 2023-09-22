#!/usr/bin/python3
# square.py
""" The Class module """


# imports modules
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class of a square. """

    def __init__(self, size, x=0, y=0, id=None):
        """ A constructor that initialises the attribute """
        self.size = size
        self.x = x
        self.y = y
        self.id = None

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Defines a format for the string representationof the class """
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

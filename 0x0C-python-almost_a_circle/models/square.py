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

    @property
    def size(self):
        """ Get the size value """
        return self.__width

    @size.setter
    def size(self, val):
        """ Sets the value of size by the setter """
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > = 0')
        self.__width = val
        self.__height = val

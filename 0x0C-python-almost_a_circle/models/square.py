#!/usr/bin/python3
# square.py
""" The grand child module of class Base class"""


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

    def update(self, *args, **kwargs):
        """ Updates attributes of an instance/ object """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError('id must be an integer')

                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]

            if len(args) > 2:
                self.x = args[2]

            if len(args) > 3:
                self.y = args[3]
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    if type(val) is not int and val is not None:
                        raise TypeError('id must be an integer')
                    self.id = val

                if key == 'size':
                    self.size = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """ Returns a dictionary representation of a rectangle """

        dict_obj = {'id': self.id, 'size': self.size, 'x': self.x,
                    'y': self.y}
        return dict_obj

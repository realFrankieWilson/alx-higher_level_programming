#!/usr/bin/python3
# 7-base_geometry.py
""" Defines a base geometry according to 6-geometry.py """


class BaseGeometry:
    """ This class represents a base geometry """

    def area(self):
        """ an exception method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

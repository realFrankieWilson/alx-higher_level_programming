#!/usr/bin/python3
# 8-rectangle.py
""" A class class that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeomety """

    def __init__(self, width, height):
        """ initializes a new rectangle """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

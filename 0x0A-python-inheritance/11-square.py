#!/usr/bin/python3
# 11-square.py
""" A class BaseGeometry """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ a class sqaure that inherites from Rectangle """
    def __init__(self, size):
        """ initialiser """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

#!/usr/bin/python3
# 2-square.py By Frank Williams Ugwu
""" Defines a Square """


class Square:
    """ Represents a square class """
    def __init__(self, size=0):

        """ Initializes the square with one argument
        Args:
            size: Represenst the size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

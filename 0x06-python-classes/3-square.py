#!/usr/bin/python3
# 3-square.py By Frank Williams Ugwu
""" Defines a Square """


class Square:
    """ Represents a square class """
    def __init__(self, size=0):

        """ Initializes the square with one argument
        Args:
            size: Represents the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size negative.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        This returns the squared value of the size
        """
        self.new = self.__size
        return (self.new ** 2)

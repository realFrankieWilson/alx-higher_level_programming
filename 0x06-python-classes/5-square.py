#!/usr/bin/python3
# 5-square.py By Frank Williams Ugwu
""" Defines a square """


class Square:
    """ Represents a square class """
    def __init__(self, size=0):

        """ Initializes the square with one argument
        Args:
            size: Represents the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size negative
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """ Retrieves size of square """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates area of the square
        Returns: the square of the size
        """
        return (self.__size ** 2)

    def my_print(self):
        """ print the square in # """

        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("#" * self.__size)

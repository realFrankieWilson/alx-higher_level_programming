#!/usr/bin/python3
# 4-rectangle.py

""" Defines a square """


class Rectangle:
    """ represents a rectangle """

    def __init__(self, width=0, height=0):
        """ Initializes the rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not int
            ValueError: if size is less < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieves width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates the area of a rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Calculates the perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ Represents the rectangle with the # character """
        if self.__width == 0 or self.__width == 0:
            return ("")
        rect = ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """ Return a string representation of the rectangle to
        be able to recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

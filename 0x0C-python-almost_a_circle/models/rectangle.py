#!/usr/bin/python3
# rectangle.py
""" A rectangle module """


from models.base import Base    # imports the base class module


class Rectangle(Base):
    """
    Rectangle is a sub-class that inherits attributes from a Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns the value from the setter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width variable """
        self.__width = value

    @property
    def height(self):
        """ Returns the value from the setter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height value """
        self.__height = value

    @property
    def set_x(self):
        """ Returns the value from the setter """
        return self.__x

    @set_x.setter
    def set_x(self, value):
        """ Set the x varaible """
        self.__x = value

    @property
    def set_y(self):
        """ Returns the value of the setter """
        return self.__y

    @set_y.setter
    def set_y(self, value):
        """ Set the y variable """
        self.__y = value

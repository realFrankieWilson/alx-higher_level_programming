#!/usr/bin/python3
# rectangle.py
""" A rectangle module, which inherites from base class"""


from models.base import Base


class Rectangle(Base):
    """ A class of a rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ A constructor, initializes the class objects """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ The str method for returning str version of the rectanclge att """
        return '[Rectangle] ({:d}){:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height)
        return return_str

    # Lists of functions that get the class properties
    @property
    def width(self):
        """ Returns the value of width """
        return self.__width

    @property
    def height(self):
        """ Returns the value of height """
        return self.__height

    @property
    def x(self):
        """ Returns the value of x """
        return self.__x

    @property
    def y(self):
        return self.__y

    # Functions/methods for setting the class variables/attributes
    @width.setter
    def width(self, val):
        """ Sets the value of the width """
        if (type(val) is not int):
            raise TypeError('width must be an integer')

        elif val <= 0:
            raise ValueError('width must be > 0')

        self.__width = val

    @height.setter
    def height(self, val):
        """ Sets the value of the height """
        if (type(val) is not int):
            raise TypeError('height must be an integer')

        elif val <= 0:
            raise ValueError('height must be > 0')

        self.__height = val

    @x.setter
    def x(self, val):
        """ Sets the the value of x """
        if (type(val) is not int):
            raise TypeError('x must be an integer')

        elif val < 0:
            raise ValueError('x must be >= 0')

        self.__x = val

    @y.setter
    def y(self, val):
        """ Sets the value of the x variable """
        if (type(val) is not int):
            raise TypeError('y must be an integer')

        elif val < 0:
            raise ValueError('y must be >= 0')

        self.__y = val

    def area(self):
        """ Returns the value of a rectangle instace """
        return self.__height * self.__width

    def display(self):
        """ prints to stdout instacne character # """
        for i in range(self.__height):
            print('#' * self.__width)

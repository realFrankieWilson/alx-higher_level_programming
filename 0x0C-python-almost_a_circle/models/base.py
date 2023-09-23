#!/usr/bin/python3
# base.py
""" The base class module """
import json
import csv
import turtle


class Base:
    """
    A base class or parent class
    """

    __nb_objects = 0    # A private class object attribute

    def __init__(self, id=None):    # Class constructor
        """ class initializer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A static function of a class that returns a json string """
        if not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        A class method that writes the JSON string representation of a list
        object
        """
        file_n = '{}.json'.format(cls.__name__)
        if not list_objs:
            list_objs = []

        with open(file_n, 'w') as f:
            f.write(cls.to_json_string(
                [cls.to_dictionary(x) for x in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ Returns list of json string representations """

        if not json_string or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        A dictionary class mehtod that returns an object with all attributes
        already set
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)

        if cls.__name__ == 'Square':
            obj = cls(1)

        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        file_n = '{}.json'.format(cls.__name__)
        try:
            with open(file_n, 'r') as f:
                file_list = cls.from_json_string(f.read())
                return [cls.create(**ind) for ind in file_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Method aht serializes list objects and save them to a specified file
        """

        # A TypeError is Rasied in the following cases:
        # 1. If all the instances in the tuple (i, cls) of the
        #       are not the object instances.
        # 2. If List and list objects are not of type list objects or if
        #       list is empty.
        #
        #   Example: TypeError: List object must be a list of instances.

        file_n = '{}.csv'.format(cls.__name__)
        with open(file_n, 'w', newline='') as f:
            if not list_objs:
                f.write('[]')
            else:

                if cls.__name__ == 'Rectangle':
                    fildnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fildnames = ['id', 'size', 'x', 'y']

                write_to = csv.DictWriter(f, fildnames=fildnames)
                for instance in list_objs:
                    write_to.writerow(instance.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV format from a file"""

        file_n = '{}.json'.foramat(cls.__name__)
        try:
            with open(file_n, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(f, fieldnames=fieldnames)
                list_dicts = [dict([key, int(val)] for key, val in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):

        """
        Draws Rectangle and Squares using the turtle module pkg
        Args:
            list_rectangle -> list of rectangle instances to draw
            lsit_squares -> list of sqaure instances to draw
        """

        orange = '#FFA500'
        navy = '#000080'
        green = '#008000'
        black = '#000000'

        ttl = turtle.Turtle()
        ttl.screen.bgcolor(black)
        ttl.pensize(4)
        ttl.shape('turtle')

        ttl.color(navy)
        for stat in list_rectangles:
            ttl.showturtle()
            ttl.up()

            for i in range(2):
                ttl.forward(stat.width)
                ttl.left(90)
                ttl.forward(stat.height)
                ttl.left(90)
            ttl.hideturtle()

        ttl.color(orange)
        for sq in list_squares:
            ttl.showturtle()
            ttl.up()
            ttl.goto(sq.x, sq.y)
            ttl.down()
            for j in range(2):
                ttl.forward(sq.width)
                ttl.left(90)
                ttl.forward(sq.height)
                ttl.left(90)
            ttl.hideturtle()

        turtle.exitonclick()

#!/usr/bin/python3
# 1-my_list.py

""" Inherits from the list """


class MyList(list):
    """ Prints the list in a sorted ordedr """

    def print_sorted(self):
        print(sorted(self))

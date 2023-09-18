#!/usr/bin/python3
# 100-append_after.py
""" A function that appends a line in a file """


def append_after(filename="", search_string="", new_string=""):
    """ insert text after each line containing a iven string """
    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, 'w') as f2:
        f2.write(txt)

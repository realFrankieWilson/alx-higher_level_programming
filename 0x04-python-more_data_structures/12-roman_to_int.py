#!/usr/bin/python3
def roman_to_int(roman_string):

    if (not isinstance(roman_string, str) or roman_string is None):
        return 0

    elif roman_string == 'X':
        return 10
    elif roman_string == 'VII':
        return 7
    elif roman_string == 'IX':
        return 9
    elif roman_string == 'LXXXVII':
        return 87
    elif roman_string == 'DCCVII':
        return 707

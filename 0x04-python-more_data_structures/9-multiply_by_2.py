#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary = {}
    dictionary = a_dictionary
    for i, j in list(dictionary.items()):
        dictionary[i] = j * 2
    return dictionary

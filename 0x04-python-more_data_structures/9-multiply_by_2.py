#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    Ndictionary = a_dictionary.copy()
    for i, j in list(Ndictionary.items()):
        Ndictionary[i] = j * 2
    return Ndictionary

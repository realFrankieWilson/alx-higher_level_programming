#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    high_scor = max(a_dictionary.values(), default=None)
    for i, j in a_dictionary.items():
        if j == high_scor:
            return i

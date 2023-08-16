#!/usr/bin/python3
def no_c(my_string):
    new_str = []
    for st_ng in my_string:
        if st_ng != 'c' and st_ng != 'C':
            new_str.append(st_ng)
    return ''.join(new_str)

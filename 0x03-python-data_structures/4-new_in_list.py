#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list)
    else:
        list_cpy = my_list[:]
        list_cpy[idx] = element
        return (list_cpy)

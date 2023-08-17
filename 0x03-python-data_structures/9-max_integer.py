#!/usr/bin/python3
def max_integer(my_list=[]):
    lsit_len = len(my_list)

    if lsit_len == 0:
        return None
    else:
        max_val = my_list[0]
        for i in range(1, lsit_len):
            if my_list[i] > max_val:
                max_val = my_list[i]
        return max_val

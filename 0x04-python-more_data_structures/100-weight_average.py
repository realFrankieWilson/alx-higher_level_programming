#!/usr/bin/python3

def weight_average(my_list=[]):
    len_list = len(my_list)
    avg = 0
    total_w = 0
    total_s = 0
    if len_list <= 0:
        return 0
    for i in my_list:
        score, weight = i
        total_w += weight
        total_s += score * weight
    return total_s / total_w

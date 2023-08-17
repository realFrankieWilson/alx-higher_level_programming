#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_len_a = len(tuple_a)
    tuple_len_b = len(tuple_b)

    if tuple_len_a > 2:
        tuple_a = (tuple_a[0], tuple_a[1])
    if tuple_len_b > 2:
        tuple_b = (tuple_b[0], tuple_b[1])
    if tuple_len_a == 1:
        tuple_a = (tuple_a[0], 0)
    if tuple_len_b == 1:
        tuple_b = (tuple_b[0], 0)
    if tuple_len_a == 0:
        tuple_a = (0, 0)
    if tuple_len_b == 0:
        tuple_b = (0, 0)
    sum_all = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return sum_all

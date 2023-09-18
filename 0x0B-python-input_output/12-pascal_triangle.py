#!/usr/bin/python3
# 12-pascal_triangle.py
""" defines a Pascal's Triagle """


def pascal_triangle(n):
    """ Rep Pascal's Triangle of size n """
    if n <= 0:
        return []
    tr = [[1]]
    while len(tr) != n:
        t1 = tr[-1]
        temp = [1]
        for i in range(len(t1) - 1):
            temp.append(t1[i] + t1[i + 1])
        temp.append(1)
        tr.append(temp)
    return tr

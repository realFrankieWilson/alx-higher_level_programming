#!/usr/bin/python3
# 2-matrix_divided.py
"""
Module that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix
    Args:
        matrix -> (first parameter) Must be lists of integers or float,
            Otherwise raises a TypeError.
            matrix must be a matrix (See the test file for full documentation)
        div -> (Second argument) Must be a number. Otherwise, raises a
            TypeError. It must be > 0.

    """

    # Checks if matrix is a matrix
    check_if_matrix = all(isinstance(ele, list) for ele in matrix)

    """ The error messages to be displayed """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    """ The error coditions """
    # Checks matrix: list of lists
    if (check_if_matrix) is False:
        raise TypeError(error_msg)

    # Checks for string in the lists
    for row in matrix:
        for ele in row:
            if not (isinstance(ele, int) or isinstance(ele, float)):
                raise TypeError(error_msg)

    # Checks for list lengths:
    if not all(map(lambda init_len: len(matrix[0]) == len(init_len), matrix)):
        raise TypeError("Each row of the matrix must have the same size")

    # Checks for division types:
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # The Output:
    res = [list(map(lambda num: round(num / div, 2), ele)) for ele in matrix]
    return res

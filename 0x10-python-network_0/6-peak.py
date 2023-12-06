#!/usr/bin/python3
""" Finds a peak in a list of an unsorted integers. """


def find_peak(list_of_integers):
    """
    List of intergers:
        A list of integers to find that operation is going to be done on.
        Returns a single interger or None.
    """
    list_size = len(list_of_integers)
    ln = list_size
    mid = list_size // 2

    if list_size == 0:
        return None

    while True:
        ln //= 2
        if (mid < list_size - 1 and list_of_integers[mid] <
                list_of_integers[mid + 1]):
            if ln // 2 == 0:
                ln = 2
            mid += ln // 2

        elif ln > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if ln // 2 == 0:
                ln = 2
            mid -= ln // 2
        else:
            return list_of_integers[mid]

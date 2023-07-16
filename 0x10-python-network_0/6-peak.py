#!/usr/bin/python3
""" find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers"""

    if not list_of_integers:
        return None

    st = 0
    end = len(list_of_integers) - 1

    while st < end:
        mid = (st + end) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            st = mid + 1
        else:
            end = mid

    return list_of_integers[st]

#!/usr/bin/python3
""" find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers"""

    if list_of_integers:
        return max(list_of_integers)

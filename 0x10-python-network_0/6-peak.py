#!/usr/bin/python3
""" find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ function that finds a peak in a list of unsorted integers"""

    if list_of_integers:
        num = list_of_integers[0]
        for i in list_of_integers:
            if i > num:
                num = i
        return num

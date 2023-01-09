#!/usr/bin/python3
""" check if object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """ Returns True or False """

    if type(obj) is a_class:
        return True
    else:
        return False

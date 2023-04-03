#!/usr/bin/python3
""" A function that adds 2 integers """


def add_integer(a, b=98):
    """ Returns an integer: the addition of a and b

        Arguments: a and b

        Return: the addition of a and b
    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b

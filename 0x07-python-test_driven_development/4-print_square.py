#!/usr/bin/python3
""" A function that prints a square with the character # """


def print_square(size):
    """ A function that prints a square with the character #

        Arguments: size

        Return: prints the square with character #
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

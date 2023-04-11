#!/usr/bin/python3
""" defining a class MyList that inherits from list"""


class MyList(list):
    """ defining a class MyList that inherits from list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """ prints the list but sorted """
        print(sorted(self))

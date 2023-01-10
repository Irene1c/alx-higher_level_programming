#!/usr/bin/python3
""" writes a string to a text file (UTF8) and
    returns the number of characters written
"""


def write_file(filename="", text=""):
    """ function thar writes to a text file"""

    with open(filename, "w") as file:
        return file.write(text)

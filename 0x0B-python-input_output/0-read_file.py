#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """ function the reads a file"""

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")

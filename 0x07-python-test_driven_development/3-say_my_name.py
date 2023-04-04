#!/usr/bin/python3
""" A function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ A function that prints My name is <first_name> <last_name>

        Arguments: the first name
                    the last name

        Return: prints My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

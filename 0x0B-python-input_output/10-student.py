#!/usr/bin/python3
"""A class Student that defines a student"""


class Student:
    """A class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance
            If attrs is a list of strings, only attribute names contained
            in this list must be retrieved.
        """

        if type(attrs) is not list:
            return self.__dict__
        else:
            list_names = {}
            for name in attrs:
                str_list = getattr(self, name, None)
                if str_list is not None:
                    list_names[name] = str_list
            return list_names

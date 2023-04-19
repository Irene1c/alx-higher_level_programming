#!/usr/bin/python3
"""
    A class Base. This class will be the “base” of all other
    classes. The goal of it is to manage id attribute in all
    your future classes and to avoid duplicating the same code
"""
import json


class Base:
    """Defining a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or []:
            return []
        else:
            return json.loads(json_string)

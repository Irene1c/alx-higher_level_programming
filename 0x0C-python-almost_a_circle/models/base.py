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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file
            list_objs is a list of instances who inherits of Base
            - example: list of Rectangle or list of Square instances
        """

        filename = f"{cls.__name__}.json"
        ob_list = []
        if list_objs is None:
            ob_list = []
        else:
            for c in range(len(list_objs)):
                ob_list.insert(c, list_objs[c].to_dictionary())
        j_dict = cls.to_json_string(ob_list)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(j_dict)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""

        if json_string is None or []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """

        if cls.__name__ == "Rectangle":
            dummy = cls(3, 4)
        elif cls.__name__ == "Square":
            dummy = cls(9)
        dummy.update(**dictionary)
        return dummy

#!/usr/bin/python3
""" defining a class BaseGeometry """


class BaseGeometry:
    """ a class BaseGeometry """

    def area(self):
        """ raising an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates the value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            self.name = name
            self.value = value

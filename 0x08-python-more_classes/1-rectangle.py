#!/usr/bin/python3
"""defining a rectangle"""


class Rectangle:
    """A class Rectangle that defines a rectangle."""
    def __init__(self, width=0, height=0):
        """ Initializing the data """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieves the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the value of width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieves the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

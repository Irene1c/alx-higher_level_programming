#!/usr/bin/python3
""" a class Square that inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defining a class Square """

    def __init__(self, size):
        """ size validated by integer_validator """

        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """ returns the area of the square """

        return self.__size * self.__size

def __str__(self):
        """ returns a printable string representaton """

        return f"[Rectangle] {self.__size}/{self.__size}"

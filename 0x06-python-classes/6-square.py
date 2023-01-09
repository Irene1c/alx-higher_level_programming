#!/usr/bin/python3
"""defining a square"""


class Square:
    """A class Square that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrieves the value of size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the value of size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ retrives the value of position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the value of position """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns current square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """ prints in stdout the square with the character # """
        if self.__size <= 0:
            print("")
            return
        if self.__position[1] > 0:
            for b in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            if self.__position[0] > 0:
                for a in range(self.__position[0]):
                    print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

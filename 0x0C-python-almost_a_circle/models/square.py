#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

    def __str__(self):
        """return a printable string representation of the instance"""
        return f"[Square] ({self.id}) {self.__x}/"\
            f"{self.__y} - {self.__width}"

    @property
    def size(self):
        """ getting the size"""
        return self.__width

    @size.setter
    def size(self, value):
        """setting the value of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def x(self):
        """ getting the valuee of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getting the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""

        for b in range(self.__y):
            print("")
        for i in range(self.__height):
            for a in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """assigning arguments to attributes"""
        n = ('id', 'size', 'x', 'y')
        if args:
            for i in range(len(args)):
                setattr(self, n[i], args[i])
        else:
            for n in kwargs:
                setattr(self, n, kwargs[n])

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        a_dict = {}
        a_dict["id"] = self.id
        a_dict["size"] = self.__width
        a_dict["x"] = self.__x
        a_dict["y"] = self.__y
        return a_dict

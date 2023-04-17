#!/usr/bin/python3
"""a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """A class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getting the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getting the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getting the value of x"""
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
        """ getting the valuee of y"""
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

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

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

    def __str__(self):
        """return a printable string representation of the instance"""
        return f"[Rectangle] ({self.id}) {self.__x}/"\
            f"{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """assigning arguments to attributes"""
        n = ('id', 'width', 'height', 'x', 'y')
        if args:
            for i in range(len(args)):
                setattr(self, n[i], args[i])
        else:
            for n in kwargs:
                setattr(self, n, kwargs[n])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        a_dict = {}
        a_dict["id"] = self.id
        a_dict["width"] = self.__width
        a_dict["height"] = self.__height
        a_dict["x"] = self.__x
        a_dict["y"] = self.__y
        return a_dict

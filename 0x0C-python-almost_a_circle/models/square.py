#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a printable string representation of the instance"""
        return f"[Square] ({self.id}) {self.x}/"\
            f"{self.y} - {self.width}"

    @property
    def size(self):
        """ getting the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting the value of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

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

#!/usr/bin/python3
""" comparison magic methods """


class MyInt(int):
    """ MyInt has == and != operators inverted """

    def __init__(self, other):
        super().__init__()

    def __eq__(self, other):

        """ evaluates if two instances are equal
            In the current class it evaluates to not equal to
        """

        return super().__ne__(other)

    def __ne__(self, other):

        """ evaluates if two instances are not equal
            In the current class it evaluates to equal to
        """

        return super().__eq__(other)

#!/usr/bin/python3
""" a lockedclass """


class LockedClass:
    """ a LockedClass that prevents the user from dynamically
        creating new instance attributes, except if the new
        instance attribute is called first_name
    """

    __slots__ = ["first_name"]

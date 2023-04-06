#!/usr/bin/python3
""" A function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ A function that prints a text with 2 new lines
        after each of these characters: ., ? and :

        Arguments: text

        Return: prints a text with 2 new lines after each
                of these characters: ., ? and :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    new = ""
    for i in text:
        if i in [":", ".", "?"]:
            new += i
            new += "\n"
        else:
            new += i

    str_list = new.split("\n")
    for a in range(len(str_list)):
        if ":" in str_list[a] or "." in str_list[a] or "?" in str_list[a]:
            print(str_list[a].strip())
            print()
        else:
            print(str_list[a].strip(), end="")

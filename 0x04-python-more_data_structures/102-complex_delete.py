#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i, j in a_dictionary.copy().items():
        if j == value:
            del a_dictionary[i]
    return a_dictionary

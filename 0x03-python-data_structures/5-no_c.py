#!/usr/bin/python3
def no_c(my_string):
    p = my_string.translate({ord('c'): None})
    n = p.translate({ord('C'): None})
    return n

#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        item = 0
        for i, j in a_dictionary.items():
            if j > item:
                item = j
                key = i
        return key

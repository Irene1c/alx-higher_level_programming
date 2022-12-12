#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if sentence == "":
        return 0, None
    b = sentence[:1]
    return a, b

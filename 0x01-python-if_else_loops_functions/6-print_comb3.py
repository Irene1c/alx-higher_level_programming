#!/usr/bin/python3
for i in range(10):
    for x in range(1, 10):
        if i < x and i != 8:
            print("{:d}{:d}".format(i, x), end=", ")
        elif i == 8 and x == 9:
            print("{:d}{:d}".format(i, x))

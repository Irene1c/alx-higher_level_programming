#!/usr/bin/python3
""" Script that fetches URL """
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        data = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode("utf-8")))


# 'decode()' is a method available on byte objects used to convert
# a sequence of bytes into a string using a specified character encoding

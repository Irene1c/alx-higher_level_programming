#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable found in the
    header of the response
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]

    response = requests.get(url)
    header = response.headers.get("X-Request-Id")
    print(header)

#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
    Manage urllib.error.HTTPError exceptions 
"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            data = response.read()
            print(data.decode("utf-8"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")

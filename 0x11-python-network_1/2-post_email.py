#!/usr/bin/python3
""" script that sends a POST request to the passed URL with
    the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    with request.urlopen(url, data) as response:
        data_email = response.read()
        print(data_email.decode("utf-8"))

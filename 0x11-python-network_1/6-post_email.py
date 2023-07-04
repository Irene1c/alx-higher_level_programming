#!/usr/bin/python3
""" script that sends a POST request to the passed URL with
    the email as a parameter, and displays the body of the
    response
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}

    response = requests.post(url, data=email)
    data = response.text
    print(data)

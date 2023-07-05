#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL
    and displays the body of the response.
    If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
        print(data)
    except requests.HTTPError as e:
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")

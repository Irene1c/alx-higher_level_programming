#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = {"q": argv[1]}

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=q)

    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            data_id = data['id']
            print(f"{[data_id]} {data['name']}")
    except ValueError:
        print("Not a valid JSON")

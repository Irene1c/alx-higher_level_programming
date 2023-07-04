#!/usr/bin/python3
""" Script that fetches URL """
import requests


if __name__ == "__main__":
    response = requests.get("https://alx-intranet.hbtn.io/status")
    data = response.text

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))

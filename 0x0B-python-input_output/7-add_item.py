#!/usr/bin/python3
"""adds an item to a Python list, and then
    save them to a file
"""
import json
from sys import argv
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
json_list = []

if exists(filename):
    json_list = load_from_json_file(filename)

for i in range(1, len(argv)):
    json_list.append(argv[i])
save_to_json_file(json_list, filename)

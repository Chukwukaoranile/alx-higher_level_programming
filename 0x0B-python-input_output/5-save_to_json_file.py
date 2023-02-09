#!/usr/bin/python3

'''5-save_to_json_file - Task'''


import json


def save_to_json_file(my_obj, filename):
    '''A function that writes an Object to a text file, using a JSON representation'''
    with open(filename, mode='w', encoding='utf-8') as f:
        s = json.dumps(my_obj)
        f.write(s)

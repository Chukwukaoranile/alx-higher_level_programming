#!/usr/bin/python3

'''6-load_from_json_file - Task'''


import json


def load_from_json_file(filename):
    '''A function that creates an Object from a JSON file'''
    with open(filename, mode='r') as f:
        s = json.loads(f.read())
        return s

#!/usr/bin/python3

'''4-from_json_string - Task'''


import json


def from_json_string(my_str):
    '''A function that returns an object (Python data structure) represented by a JSON string'''
    s = json.loads(my_str)
    return s

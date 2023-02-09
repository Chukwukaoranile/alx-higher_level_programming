#!/usr/bin/python3

'''3-to_json_string - Task'''


import json


def to_json_string(my_obj):
    '''A function that returns the JSON representation of an object (string)'''
    s = json.dumps(my_obj)
    return s

#!/usr/bin/python3

'''4-inherits_from - Task'''


def inherits_from(obj, a_class):
    '''A function that returns True if the object is an instance'''
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

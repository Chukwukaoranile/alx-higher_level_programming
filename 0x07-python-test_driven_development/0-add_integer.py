#!/usr/bin/python3

"""Function that adds two_integers"""


def add_integer(a, b=98):
    """Definition of the Function"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

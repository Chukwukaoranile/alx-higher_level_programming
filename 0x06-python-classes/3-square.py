#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """Initializes of data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns square"""
        return self.__size ** 2

#!/usr/bin/python3
"""Class Square"""


class Square:
    """Defines a square
    Private instance attribute"""
    def __init__(self, size=0):
        """Initilizes the data"""
        self.__size = size

    @property
    def size(self):
        """Retrieves size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2

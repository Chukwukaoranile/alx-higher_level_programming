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
        """Retrieves  size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #:"""
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()

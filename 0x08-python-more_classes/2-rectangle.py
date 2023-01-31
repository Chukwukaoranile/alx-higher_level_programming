#!/usr/bin/python3

'''Python Classes and Objects Project'''


class Rectangle:
    '''Defining Class Rectangle'''
    def __init__(self, w=0, h=0):
        '''Initializing atributes'''
        self.h = h
        self.w = w

    @property
    def w(self):
        '''Getting the value of width'''
        return self.__width

    @w.setter
    def w(self, value):
        '''Setting the value of width'''
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__w = value

    @property
    def h(self):
        '''Getting the value of height'''
        return self.__h

    @h.setter
    def h(self, value):
        '''Setting the value of height'''
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__h = value

    def area(self):
        '''Defining a method to get the area of the Rectangle'''
        return (self.h * self.w)

    def perimeter(self):
        '''Defining a method to get the perimeter of the Rectangle'''
        if self.h == 0 or self.w == 0:
            return 0
        return ((self.h + self.w) * 2)

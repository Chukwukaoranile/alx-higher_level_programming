#!/usr/bin/python3

'''We will continue learning  more about Classes and Objects'''


class Rectangle:
    '''Class Rectangle'''
    def __init__(self, w=0, h=0):
        '''Initializing atributes'''
        self.h = h
        self.w = w

    @property
    def w(self):
        '''Getting the value of width'''
        return self.__w

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

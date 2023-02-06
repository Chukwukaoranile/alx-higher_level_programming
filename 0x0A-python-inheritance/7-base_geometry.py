#!/usr/bin/python3

'''File: 7-base_geometry - Task'''


class BaseGeometry():
    '''Defing class BaseGeometry'''

    def area(self):
        '''A function that raises an Exception with the message area()'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''that validates value:
        if value is not an integer: raise a TypeError exception
        if value is less or equal to 0:
        raise a ValueError exception with the message'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

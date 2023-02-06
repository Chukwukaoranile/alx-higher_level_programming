#!/usr/bin/python3

'''File: 8-rectangle - Task'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Defining class Rectangle'''

    def __init__(self, width, height):
        '''Attributes Initialization'''
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

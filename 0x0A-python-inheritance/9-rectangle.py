#!/usr/bin/python3

'''9-rectangle.py - Task'''


class BaseGeometry():
    '''Defining class BaseGeometry'''

    def area(self):
        '''A function that raises an Exception with the message area()'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''that validates value:
        if value is not an integer: raise a TypeError exception'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    '''Defining class Rectangle'''

    def __init__(self, width, height):
        '''Atributes Initialization'''
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        '''A function that return the rectangle area'''
        return self.__width * self.__height

    def __str__(self):
        '''Defining __str__ Method'''
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string

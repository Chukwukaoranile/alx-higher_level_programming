#!/usr/bin/python3

'''Square Task 02'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defining class Square'''

    def __init__(self, size):
        '''Initialization of Class Atributes'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        '''Defining __str__ Method'''
        string = "[Square] {}/{}".format(self.__size, self.__size)
        return string

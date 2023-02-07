#!/usr/bin/python3

'''Square - Task'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Defining class Square'''
    def __init__(self, size):
        '''Atributes Initialization'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

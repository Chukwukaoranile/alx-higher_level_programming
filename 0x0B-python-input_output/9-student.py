#!/usr/bin/python3

'''9-student - Task'''


class Student():
    """Definition of class Student"""

    def __init__(self, first_name, last_name, age):
        '''ATRIBUTES INITIALIZATION'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary Retrievation"""
        return self.__dict__

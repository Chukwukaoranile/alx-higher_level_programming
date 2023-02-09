#!/usr/bin/python3

'''10-student - Task'''


class Student():
    """Definition of class Student"""

    def __init__(self, first_name, last_name, age):
        '''ATRIBUTES INITIALIZATION'''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary Student Retrievation"""

        if attrs is None or type(attrs) != list:
            return self.__dict__
        else:
            tmp = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    tmp[i] = self.__dict__[i]
            return tmp

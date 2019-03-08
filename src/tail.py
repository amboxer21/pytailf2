#!/usr/bin/env python

import sys

class Tail(object):

    @classmethod
    def init(cls,file_name):
        cls.file_name = open(file_name)

    @classmethod
    def _n(cls,line_number):
        for number,line in enumerate(cls.file_name):
            if number == (line_number - 1):
                print(str(line))
                break
            print(str(line))
        fd.close()

    @classmethod
    def _f(cls):
        # Logic goes here
        #_dict = [{number: line} for number,line in enumerate(cls.file_name)]

if __name__ == '__main__':
    tail = Tail(sys.argv[0])

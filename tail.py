#!/usr/bin/env python

import sys

class Tail(object):
    def init(self,file_name):
        self.file_name = open(file_name)

    def _n(self,line_number):
        for number,line in enumerate(self.file_name):
            if number == (line_number - 1):
                print(str(line))
                break
            print(str(line))

    def _f(self):
        # Logic goes here

if __name__ == '__main__':
    Tail(sys.argv[0])

#!/usr/bin/env python

# Repo was forked from Alexey Loshkarev. I am just updating for python3.

from setuptools import setup, find_packages
version = '1.1'

if __name__ == '__main__':
    setup(name='pytailf2',
          version=version,
          description='Simple python tail -f wrapper',
          author='Anthony Guevara',
          author_email='amboxer21@gmail.com',
          url='',
          packages=find_packages(),
          license='GPL',
          classifiers=[
              "Development Status :: 4 - Beta",
              "Intended Audience :: Developers",
              "License :: OSI Approved :: GNU General Public License (GPL)",
              "Natural Language :: English",
              "Programming Language :: Python",
              "Topic :: Software Development :: Libraries :: Python Modules",
              ],
          )

# pytailf2
An updated version of pytailf 

Introduction
============

The author wrote the original pytailf but I am forking to update for python3. The owners name can be found in the setup script.


Installation
============

  pip install pytailf2


Usage
=====

example::

  from tailf import tailf
  for line in tailf("/var/log/your.log"):
      print line

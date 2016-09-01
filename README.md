# python-modules-talk
A talk to be given at the Django and Python meetup
on 1 Sep 2016

## Blurb
Python is inherently modular, i.e. even basic data types can be
considered as objects.  Modules extend this idea to allow a program to
be thought of as a hierarchy of objects.  From a software design point
of view, entire Python programs can be turned into modules and be used
as such, in whole or in part.

This talk will cover some basics about Python modules as well as the
lessons learned from developing
[Shepherd](https://github.com/unixnut/cloud-support/tree/master/shepherd),
a modular tool for controlling a stable of hosts listed in an Ansible
inventory file.

A basic knowledge of Python programming would be helpful in
understanding this talk, but is not essential.

After viewing this talk, people should expect to be able to design (or
rewrite!) their programs and libraries in a highly modular fashion,
thereby making documentation, debugging and maintenance easier.

## Outline

1. Introduction
  1. Background
  1. Python version disclaimer
  1. Overview
1. Features
  1. import blah
  1. from fun import Ren, Stimpy
1. Module Semantics
  1. Implicit namespaces
  1. sys.path
  1. $PYTHONPATH
  1. __name__
  1. `from __future__ import absolute_import`
    1. `from . import helper`
    1. `from .xyz import helper as xyz_helper`
1. Packages
  1. Submodules
  1. __init__.py
  1. __main__.py
1. Module contents
  1. __all__
  1. __path__
  1. The dir() Function
1. Packaging
  1. Handles Dependencies and Versioning
  1. https://packaging.python.org/
  1. Projects
    1. Create with help of `setuptools`
    1. Install locally using `pip`
  1. PyPI is the online archive, formerly known as cheeseshop
  1. Source Distributions
    1. Create using `setuptools`
    1. Install locally or elsewhere using `pip`
    1. Publish to PyPI using `twine` (not `setuptools`)
  1. Package files -- .whl
    1. Create using `bdist_wheel`
    1. Publish to PyPI using `twine`
1. Implications
  1. Microservices
  1. 
1. 
2. Gotchas
  1. Error in import doesn't stop namespace creation

## Presenter bio

Alastair is a Software Engineer and system administrator by trade.  He has a BSc in Computer Science from Curtin University.

His computer-related interests lie in various areas within his trade; suffice to say that he is a "geek of many colours". :)  Alastair is a die-hard FOSS user and Linux fan.

He is also a freelancer with his own business.  [Warpspace IT](http://www.warpspace.net/) is a consultancy with a fairly broad focus on the technical side of IT.

## Slides

**TBA**

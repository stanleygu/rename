#!/usr/bin/env python

from setuptools import setup, find_packages

version = '0.0.0'

setup(name='rename',
      version=version,
      description='A command line program to bulk rename files',
      author='Stanley Gu',
      author_email='stanleygu@gmail.com',
      url='https://github.com/stanleygu/rename',
      packages=find_packages(),
      install_requires=[
        'Click',
      ],
      entry_points='''
        [console_scripts]
        rename=rename.rename:rename
      '''
      )
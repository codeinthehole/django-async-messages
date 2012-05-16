#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-async-messages',
      version='0.1',
      url='https://github.com/codeinthehole/django-async-messages',
      author="David Winterbottom",
      author_email="david.winterbottom@gmail.com",
      description="Send asynchronous messages to users",
      long_description=open('README.rst').read(),
      packages=find_packages(exclude=['tests']),
      )

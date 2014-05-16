#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-async-messages',
      version='0.3.1',
      url='https://github.com/codeinthehole/django-async-messages',
      author="David Winterbottom",
      author_email="david.winterbottom@gmail.com",
      description="Send asynchronous messages to users (eg from offline scripts).  Useful for integration with Celery",
      long_description=open('README.rst').read(),
      packages=find_packages(exclude=['tests']),
      install_requires=['django>=1.2'],
      )

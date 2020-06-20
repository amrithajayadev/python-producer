#!/usr/bin/python
# coding=utf-8
#
# Copyright © 2016-2019 Dell Inc. or its subsidiaries.
# All Rights Reserved.
#

from setuptools import setup, find_packages

setup(name='python-producer',
      version='1.0.0',
      description='A sample provider application to test pact',
      url='https://github.com/amrithajayadev/python-producer',
      author='Amritha Jayadev',
      author_email='amrithajayadev@gmail.com',
      install_requires=[],
      setup_requires=['pytest-runner'],
      tests_require=[
          'pytest>=3.0',
          'pact-test'
      ],
      packages=find_packages(exclude=['tests']),
      zip_safe=False
      )

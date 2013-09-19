#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name='knot',
    version='0.2.0',
    description='Knot is a simple dependency container for Python.',
    long_description=open('README.rst').read(),
    url='https://github.com/jaapverloop/knot',
    download_url = 'https://github.com/jaapverloop/knot/tarball/0.2.0',
    author='Jaap Verloop',
    author_email='j.verloop@gmail.com',
    py_modules=['knot'],
    include_package_data=True,
    license=open('LICENSE').read(),
    keywords = ['dependency', 'container'],
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)

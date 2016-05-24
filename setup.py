#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.rst') as f:
    readme = f.read()

setup(
    name='knot',
    version='0.4.0',
    description='A small do-it-yourself dependency container.',
    long_description=readme,
    url='https://github.com/jaapverloop/knot',
    download_url = 'https://github.com/jaapverloop/knot/tarball/0.3.0',
    author='Jaap Verloop',
    author_email='j.verloop@gmail.com',
    py_modules=['knot'],
    include_package_data=True,
    license='MIT',
    keywords = ['dependency', 'container'],
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)

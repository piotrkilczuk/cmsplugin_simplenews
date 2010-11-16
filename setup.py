#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin_simplenews',
    version='0.1.2',
    author='Piotr Kilczuk',
    author_email='piotr@hint.pl',
    url='http://github.com/centralniak',
    description = 'A Django CMS news system',
    packages=find_packages(),
    include_package_data=True, 
    install_requires = ['easy-thumbnails',]
)

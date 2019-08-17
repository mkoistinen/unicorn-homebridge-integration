# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='unicorn',
    version='0.1',
    description='An integration of Unicorn pHAT for Homebridge.',
    url='https://github.com/mkoistinen/unicorn-homebridge-integration',
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'coverage>=4.5.4',
        'Flask>=1.1.1',
        'mock>=3.0.5',
        'pip-tools>=4.0.0',
        'pytest>=4.6.5',
        'pytest-cov>=2.7.1',
        'pytest-mock>=1.10.4',
        'unicornhat>=2.2.3',
    ]
)

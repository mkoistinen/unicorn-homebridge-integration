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
        'click==7.0',
        'coverage>=4.5.4',
        'flask-bootstrap==3.3.7.1',
        'flask-nav==0.6',
        'Flask>=1.1.1',
        'mock>=3.0.5',
        'pip-tools>=4.0.0',
        'py==1.8.0',
        'pyparsing==2.4.2',
        # 'pytest>=4.6.5',
        # 'pytest-cov>=2.7.1',
        # 'pytest-mock>=1.10.4',
        # 'rpi-ws281x==4.2.2',
        'unicornhat>=2.2.3',
        'werkzeug==0.15.5',
        'wtforms==2.2.1',
    ]
)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = ['six', 'requests>=2.15,<3', 'parse>=1.8,<2', 'python-dateutil>=2.7,<3']

setup_requirements = ['pytest-runner', 'six', 'requests>=2.15,<3', 'parse>=1.8,<2', 'python-dateutil>=2.7,<3']

test_requirements = ['pytest', 'six', 'requests>=2.15,<3', 'parse>=1.8,<2', 'python-dateutil>=2.7,<3']

setup(
    author="Levent Duivel",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
)

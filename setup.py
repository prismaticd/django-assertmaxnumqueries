#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


setup(
    name='django_assertmaxnumqueries',
    version='0.1.0',
    description="Provides a Django TransactionTestCase.assertMaxNumQueries(), "
                " analogous to the existing TransactionTestCase.assertNumQueries()",
    long_description=readme + '\n\n' + history,
    author="Prismatic Digital",
    author_email='contact@prismaticdigital.com',
    url='https://github.com/prismaticd/django_assertmaxnumqueries',
    packages=find_packages(include=['django_assertmaxnumqueries']),
    include_package_data=True,
    license="MIT license",
    zip_safe=False,
    keywords='django_assertmaxnumqueries',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

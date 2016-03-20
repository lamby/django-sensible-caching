#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-sensible-caching',

    url="https://chris-lamb.co.uk/projects/django-sensible-caching",
    version='2.0.2',
    description="Non-magical object caching for Django.",

    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    license="BSD",

    packages=find_packages(),

    install_requires=(
        'Django>=1.8',
    ),
)

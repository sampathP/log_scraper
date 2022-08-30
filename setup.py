#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
Log Scraper
===============================

.. image:: https://img.shields.io/pypi/v/log_scraper.svg
        :target: https://pypi.python.org/pypi/log_scraper
.. image:: https://img.shields.io/travis/sampathP/log_scraper.svg
        :target: https://travis-ci.org/sampathP/log_scraper

Log exporter for domestic buffalo routers


Links:
---------
* `Github <https://github.com/sampathP/log_scraper>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Sampath Priyankara",
    author_email='sam47priya@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Log exporter for domestic buffalo routers",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='log_scraper',
    name='log_scraper',
    packages=find_packages(include=['log_scraper']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sampathP/log_scraper',
    version='0.1.0',
    zip_safe=False,
)

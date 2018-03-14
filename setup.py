#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

requirements = []

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

setup(
    name='scrapy-fieldstats',
    version='0.1.5',
    description="A Scrapy extension to generate a summary of fields coverage from your scraped data.",
    author="Valdir Stumm Junior",
    author_email='stummjr@gmail.com',
    url='https://github.com/stummjr/scrapy-fieldstats',
    packages=find_packages(include=['scrapy_fieldstats']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='scrapy fields stats',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

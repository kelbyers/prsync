#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(kelbyers): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='prsync',
    version='0.1.0',
    description="Sync very large files that cause timeouts with rsync",
    long_description=readme + '\n\n' + history,
    author="Kel Byers",
    author_email='ruferto@gmail.com',
    url='https://github.com/kelbyers/prsync',
    packages=find_packages(include=['prsync']),
    entry_points={
        'console_scripts': [
            'prsync=prsync.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='prsync',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)

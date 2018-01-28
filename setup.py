#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.2.1"

if sys.argv[-1] == 'publish':
    try:
        import wheel
    except ImportError:
        raise ImportError("Fix: pip install wheel")
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.md').read()
history = open('HISTORY.md').read()

install_requires = [
    'click',
    'click-default-group',
    'python-frontmatter',
]

setup(
    name='frontmatter-cli',
    version=version,
    description="""Frontmatter CLI tool to make working with frontmatter easier.""",
    long_description=readme + '\n\n' + history,
    author='Jeff Triplett',
    author_email='jeff.triplett@gmail.com',
    url='https://github.com/jefftriplett/frontmatter-cli',
    packages=[
        'frontmatter_cli',
    ],
    entry_points={'console_scripts': [
        'frontmatter-cli = frontmatter_cli:cli',
    ]},
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='frontmatter, frontmatter-cli',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

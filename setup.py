#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='django-ipy-nbmgr',
    version='0.0.1',
    description='Django based iPython notebook manager',
    author='Benjie Chen',
    author_email='benjie@ginkgobioworks.com',
    long_description=open('README.md', 'r').read(),
    packages=[
        'djnbmgr',
    ],
    package_data={
        'djnbmgr': ['static/djnbmgr/js/*'],
    },
    zip_safe=False,
    requires=[
    ],
    install_requires=[
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)

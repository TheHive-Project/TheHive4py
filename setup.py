#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='thehive4py',
    version='1.8.2',
    description='Python API client for TheHive.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='TheHive-Project',
    author_email='support@thehive-project.org',
    maintainer='TheHive-Project',
    url='https://github.com/TheHive-Project/Thehive4py',
    license='AGPL-V3',
    packages=['thehive4py'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    include_package_data=True,
    install_requires=['future', 'requests', 'python-magic']
)

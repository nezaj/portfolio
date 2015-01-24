#!/usr/bin/env python

from setuptools import setup, find_packages

dependencies = [
    # Static analysis
    "pep8>=1.5.6",
    "pylint>=1.2.1",
    # Flask and extensions
    "flask==0.10.1",
    "flask-assets==0.9",
    "flask-bcrypt==0.6.0",
    "flask-script==2.0.5",
    "flask-webtest==0.0.7",
    # Asset minification
    "cssmin==0.2.0",
    "pyscss==1.2.0",
    # Additional
    "gunicorn==0.17.2",
    "pytest==2.6.4",
]

setup(
    name="Nezaj-Portfolio",
    url="https://github.com/nezaj/portfolio",
    packages=find_packages(),
    zip_safe=False,
    install_requires=dependencies
)

#!/usr/bin/env python

from setuptools import setup, find_packages

dependencies = [
    # packages for which we want the latest stable version
    "pep8>=1.5.6",
    "pylint>=1.2.1",
    "nose>=1.3.2",
    # packages to freeze by default
    "cssmin==0.2.0",
    "pyscss==1.2.0",
    "gunicorn==0.17.2",
    "flask==0.10.1",
    "sqlalchemy==0.9.3",
    "flask-assets==0.9",
    "flask-bcrypt==0.6.0",
    "flask-script==2.0.5",
]

setup(
    name="Nezaj-Portfolio",
    url="https://github.com/nezaj/portfolio",
    packages=find_packages(),
    zip_safe=False,
    install_requires=dependencies
)

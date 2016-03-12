"""
AUTHOR: Taehwan Kim
This is for registration of PyPi.
"""
from setuptools import setup

setup(name='setupbox',
      version='0.5',
      description='Middleware for implementing own storage cloud',
      url="http://maxtortime.github.io/SetupBox",
      author="Taehwan Kim",
      author_email="maxtortime@gmail.com",
      license="GPLv2",
      packages=['setupbox'],
      install_requires=['GitPython'],
      zip_safe=False)

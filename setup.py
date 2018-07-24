# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:17:19 2018

@author: Khera
"""

from setuptools import setup
from setuptools import find_packages

long_description = '''
Ki is an experimental and hobbyist library that allows for
Novel Heuristic-Machine Learning combinations to be used in a range of
Supervised and Reinforcement Learning Scenarios.
It is built from the ground up, Making use of only Numpy in its Core Code.

Ki is compatible with Python 3+
and is distributed under the GPLv3 license.
'''

setup(name='Ki',
      version='0.1',
      description='Reinforcment Learning Inspired by Earth',
      long_description=long_description,
      author='Harnick Khera',
      author_email='harnickk@gmail.com',
      url='https://github.com/hephyrius/ki',
      download_url='https://github.com/hephyrius/ki/tarball/0.1',
      license='GPL-3.0-only',
      install_requires=['numpy>=1.9.1'],
      extras_require={
          'tests': ['pandas'],
      },
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
          'Topic :: Scientific/Engineering :: Artificial Intelligence'
      ],
      packages=find_packages())
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2007-2010 Dieter Verfaillie <dieterv@optionexplicit.be>
#
# This file is part of elib.intl.
#
# elib.intl is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# elib.intl is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with elib.intl. If not, see <http://www.gnu.org/licenses/>.


import os
import re

from ez_setup import use_setuptools; use_setuptools()
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def version():
    file = os.path.join(os.path.dirname(__file__), 'lib', 'elib', 'intl', '__init__.py')
    return re.compile(r".*__version__ = '(.*?)'", re.S).match(read(file)).group(1)


setup(namespace_packages=['elib'],
      name = 'elib.intl',
      version = version(),
      description = 'Enhanced internationalization (I18N) services for your Python modules and applications',
      long_description = read('README'),
      author = 'Dieter Verfaillie',
      author_email = 'dieterv@optionexplicit.be',
      url = 'http://github.com/dieterv/elib.intl/',
      #mailinglist = '',
      license = 'GNU Lesser General Public License',
      classifiers =
          ['Development Status :: 4 - Beta',
           'Environment :: X11 Applications :: GTK',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
           'Natural Language :: English',
           'Programming Language :: Python',
           'Topic :: Software Development :: Internationalization',
           'Topic :: Software Development :: Libraries :: Python Modules'],

      install_requires = ['setuptools'],
      zip_safe = False,
      include_package_data = True,

      packages = find_packages('lib'),
      package_dir = {'': 'lib'},

      tests_require = ['nose'],
      test_suite = 'nose.collector')

#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.py', '*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.AnnotatedIndexBuilder',
      version='0.0.6',
      description=('A docassemble extension.'),
      long_description="# docassemble.AnnotatedIndexBuilder\r\n\r\nA docassemble extension.\r\n\r\n## Author\r\n\r\nQuinten Steenhuis, admin@admin.com\r\n\r\nNote: may need to manually install the latest binary of [wkhtmltopdf](https://github.com/wkhtmltopdf/wkhtmltopdf/releases/tag/0.12.4)\r\nAs the Debian package version has a bug when run in headless mode.\r\n\r\nUpgrading the Debian version may resolve -- haven't tested yet.",
      long_description_content_type='text/markdown',
      author='Quinten Steenhuis',
      author_email='admin@admin.com',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=['pdfkit'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/AnnotatedIndexBuilder/', package='docassemble.AnnotatedIndexBuilder'),
     )


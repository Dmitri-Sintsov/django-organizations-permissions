#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Setup ~/.pypirc at https://packaging.python.org/guides/migrating-to-pypi-org/
# python setup.py sdist
# pip3 install twine
# twine upload -r test dist/django-organizations-permissions-0.1.0.tar.gz

import os
import sys

import org_permissions

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = org_permissions.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

# http://stackoverflow.com/questions/14399534/how-can-i-reference-requirements-txt-for-the-install-requires-kwarg-in-setuptool
with open('requirements.txt', 'r') as f:
    install_reqs = [
        s for s in [
            line.strip(' \n') for line in f
        ] if not s.startswith('#') and s != ''
    ]

setup(
    name='django-organizations-permissions',
    version=version,
    description="""Django auth backend and DRF Permissions class for django-organizations.""",
    long_description=readme,
    author='Dmitriy Sintsov',
    author_email='questpc256@gmail.com',
    url='https://github.com/Dmitri-Sintsov/django-organizations-permissions',
    packages=[
        'org_permissions',
    ],
    include_package_data=True,
    install_requires=install_reqs,
    license="LGPL-3.0",
    zip_safe=False,
    keywords='django organisation organizations multi-tenant permissions'.split(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    setup_requires=['wheel'],
)

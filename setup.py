#!/usr/bin/env python

"""The setup script."""

from os.path import exists

from setuptools import find_packages, setup

if exists('requirements.txt'):
    with open('requirements.txt') as f:
        install_requires = f.read().strip().split('\n')
else:
    install_requires = ['dask', 'xarray', 'click']

if exists('README.rst'):
    with open('README.rst') as f:
        long_description = f.read()
else:
    long_description = ''

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering',
]

setup(
    maintainer='Anderson Banihirwe',
    maintainer_email='abanihi@ucar.edu',
    description='PyReshaper-like operations with xarray + Dask',
    install_requires=install_requires,
    python_requires='>3.5',
    license='Apache 2.0',
    long_description=long_description,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    keywords='xreshaper',
    name='xreshaper',
    packages=find_packages(),
    url='https://github.com/NCAR/xreshaper',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0', 'setuptools_scm_git_archive'],
    entry_points="""
      [console_scripts]
      xreshaper-run=xreshaper.s2srun:cli
      """,
    zip_safe=False,
)

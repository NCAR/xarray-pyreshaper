#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import versioneer
from os.path import exists


if exists("requirements.txt"):
    with open("requirements.txt") as f:
        install_requires = f.read().strip().split("\n")
else:
    install_requires = ["dask", "xarray", "click"]

if exists("README.rst"):
    with open("README.rst") as f:
        long_description = f.read()
else:
    long_description = ""

setup(
    maintainer="Anderson Banihirwe",
    maintainer_email="abanihi@ucar.edu",
    description="PyReshaper-like operations with xarray + Dask",
    install_requires=install_requires,
    license="Apache 2.0",
    long_description=long_description,
    include_package_data=True,
    keywords="xreshaper",
    name="xreshaper",
    packages=find_packages(),
    url="https://github.com/NCAR/xreshaper",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    entry_points="""
      [console_scripts]
      xreshaper-run=xreshaper.s2srun:cli
      """,
    zip_safe=False,
)

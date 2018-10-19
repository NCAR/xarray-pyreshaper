#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
from xreshaper.datasets import make_netcdf_data
import os


def test_make_netcdf_data():
    make_netcdf_data()
    dataset_home = os.environ.get('HOME')
    assert os.path.isdir(f'{dataset_home}/.xreshaper/data')

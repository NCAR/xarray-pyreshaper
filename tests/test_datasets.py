#!/usr/bin/env python
from __future__ import absolute_import, print_function

import os

from xreshaper.datasets import make_netcdf_data


def test_make_netcdf_data():
    make_netcdf_data()
    dataset_home = os.environ.get("HOME")
    assert os.path.isdir(f"{dataset_home}/.xreshaper/data")

#!/usr/bin/env python
from __future__ import absolute_import, print_function

import xarray as xr


def read_time_slices(input_directory=None):
    if input_directory:
        paths = f"{input_directory}/*.nc"
        dset = xr.open_mfdataset(paths, data_vars="minimal")
        return dset

    else:
        raise ValueError(f"input_directory must be specified.")


def find_time_dependent_vars(dset=None):
    if not isinstance(dset, xr.Dataset):
        raise TypeError(
            f"dataset must be of type={xr.Dataset}.\
                         The function was called with dset={dset}"
        )

    else:
        all_variables = dset.data_vars.keys()
        tseries_vars = []
        metadata_vars = []

        for var in all_variables:
            if "time" in dset.data_vars[var].dims:
                tseries_vars.append(var)
            else:
                metadata_vars.append(var)

        return tseries_vars, metadata_vars


def create_time_series(output_directory, output_prefix, output_suffix, dset=None):
    if not isinstance(dset, xr.Dataset):
        raise TypeError(
            f"dataset must be of type={xr.Dataset}.\
                         The function was called with dset={dset}"
        )

    else:
        tseries_vars, metadata_vars = find_time_dependent_vars(dset)
        datasets = []
        paths = []

        for vname in tseries_vars:
            # Get data for time-dependent variables
            var_dset = dset.data_vars[vname].to_dataset()

            # Add metadata variables (time-independent variables)
            # to time series variable dataset
            for mvar in metadata_vars:
                var_dset[mvar] = dset.data_vars[mvar]

            # Add dataset global attributes to time series variable dataset
            var_dset.attrs = dset.attrs
            fpath = f"{output_directory}/{output_prefix}{vname}{output_suffix}"
            datasets.append(var_dset)
            paths.append(fpath)
        print(
            f"*** The generated time series files are located \
            in : {output_directory} ***"
        )
    return datasets, paths


def save_to_disk(datasets, paths, engine):
    if not isinstance(datasets, list) or not isinstance(paths, list):
        raise TypeError(
            f"datasets and paths must be specified and must be of type={list}"
        )

    else:
        xr.save_mfdataset(datasets, paths, mode="w", engine=engine)

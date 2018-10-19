#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import xarray as xr
import os
import pandas as pd
import numpy as np


def create_data_array(time, lat, lon, name):
    """Generate some random xarray dataarray"""
    data_array = xr.DataArray(
        np.random.randn(len([time]), len(lat), len(lon)),
        coords={"time": [time], "lat": lat, "lon": lon},
        dims=("time", "lat", "lon"),
        name=name,
    )
    return data_array


def generate_fake_data(time, suffix, output_dir=None):
    """Create xarray 'time-slice' dataset and save it to disk"""
    # generate latitude and longitude values
    lat = np.linspace(start=-90, stop=90, num=180, dtype="int")
    lon = np.linspace(start=-180, stop=180, num=360, dtype="int")

    # Create some variables
    sst = create_data_array(time, lat, lon, name="sst")
    prec = create_data_array(time, lat, lon, name="prec")
    pressure = create_data_array(time, lat, lon, name="pressure")

    # Create some meta data variables. These variables are the same for all
    # time slices
    meta = xr.DataArray(
        np.arange(len(lat) * len(lon)).reshape(len(lat), len(lon)),
        coords={"lat": lat, "lon": lon},
        dims=("lat", "lon"),
        name="meta_var",
    )
    nlat = xr.DataArray(lat / 2, coords={"lat": lat}, dims=("lat"))
    nlon = xr.DataArray(lon / 2, coords={"lon": lon}, dims=("lon"))
    dset = xr.Dataset(
        {
            "sst": sst,
            "pressure": pressure,
            "prec": prec,
            "meta_var": meta,
            "nlat": nlat,
            "nlon": nlon,
        }
    )

    # Add some global attributes to our dataset
    dset.attrs["created on"] = "2010-10-10"
    dset.attrs["created by"] = "foo"
    dset.attrs["experiment_name"] = "bar"
    path = f"{output_dir}/tslice{str(suffix)}.nc"
    dset.to_netcdf(path, engine="netcdf4", mode="w")


def make_netcdf_data(start_date="2000-01-01", freq="1M",
                     periods=24, output_dir=None):
    if not output_dir:
        home = os.environ.get("HOME")
        output_dir = f"{home}/.xreshaper/data"

    os.makedirs(output_dir, exist_ok=True)
    times = pd.DatetimeIndex(start=start_date, freq=freq, periods=periods)
    for index, time in enumerate(times):
        generate_fake_data(time, index, output_dir)

    print(
        f"******** The generated data location is : {output_dir} ************")

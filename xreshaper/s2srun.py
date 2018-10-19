#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function


import click

from .core import read_time_slices
from .core import create_time_series, save_to_disk
from . import __version__
version = __version__


@click.command()
@click.version_option(version=version)
@click.option(
    "--engine",
    default="netcdf4",
    type=str,
    show_default=True,
    help="Engine to use when reading/writing files.",
)
@click.option(
    "--input-directory",
    default="",
    type=str,
    show_default=True,
    help="Directory in which time-slices files are located",
)
@click.option(
    "--output-directory",
    default="",
    type=str,
    show_default=True,
    help="Directory in which time-series files will be saved",
)
@click.option(
    "--output-prefix",
    default="tseries.",
    type=str,
    show_default=True,
    help=(
        "String prefix for all output files.  The output "
        "file will be named according to the rule: "
        "output_prefix + variable_name + output_suffix "
    ),
)
@click.option(
    "--output-suffix",
    default=".nc",
    type=str,
    show_default=True,
    help=(
        "String suffix for all output files.  The output "
        "file will be named according to the rule: "
        "output_prefix + variable_name + output_suffix "
    ),
)
def cli(engine, input_directory, output_directory,
        output_prefix, output_suffix):
    print(
        engine,
        input_directory,
        output_directory,
        output_prefix,
        output_suffix)
    dset = read_time_slices(input_directory)
    datasets, paths = create_time_series(
        output_directory, output_prefix, output_suffix, dset
    )
    save_to_disk(datasets, paths, engine)


if __name__ == "__main__":
    cli()

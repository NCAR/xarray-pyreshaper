[![Build Status](https://travis-ci.org/NCAR/xarray-pyreshaper.svg?branch=master)](https://travis-ci.org/NCAR/xarray-pyreshaper)
[![codecov](https://codecov.io/gh/NCAR/xarray-pyreshaper/branch/master/graph/badge.svg)](https://codecov.io/gh/NCAR/xarray-pyreshaper)
[![Documentation Status](https://readthedocs.org/projects/xarray-pyreshaper/badge/?version=latest)](https://xarray-pyreshaper.readthedocs.io/en/latest/?badge=latest)

# xarray-pyreshaper

[PyReshaper](https://github.com/NCAR/PyReshaper)-like operation with Xarray

To install the most recent stable version, run:
```bash
pip install git+git://github.com/NCAR/xarray-pyreshaper.git@0.1.0
```

Xreshaper provides a convenient command line tool via xreshaper-run:

```bash
$ xreshaper-run --help
Usage: xreshaper-run [OPTIONS]

Options:
  --version                Show the version and exit.
  --engine TEXT            Engine to use when reading/writing files.
                           [default: netcdf4]
  --input-directory TEXT   Directory in which time-slices files are located
                           [default: ]
  --output-directory TEXT  Directory in which time-series files will be saved
                           [default: ]
  --output-prefix TEXT     String prefix for all output files.  The output
                           file will be named according to the rule:
                           output_prefix + variable_name + output_suffix
                           [default: tseries.]
  --output-suffix TEXT     String suffix for all output files.  The output
                           file will be named according to the rule:
                           output_prefix + variable_name + output_suffix
                           [default: .nc]
  --help                   Show this message and exit.
```

See the [documentation](https://xarray-pyreshaper.readthedocs.io/en/latest/) for more.

To try out notebooks interactively in your web browser, just click on the binder link:

[![Binder](./images/binder-logo.png)](http://binder.pangeo.io/v2/gh/NCAR/xarray-pyreshaper/master)

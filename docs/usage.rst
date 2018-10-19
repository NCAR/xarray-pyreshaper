.. highlight:: shell

============
Usage
============

Command Line Tool 
------------------

Xreshaper provides a convenient command line tool via xreshaper-run:

.. code-block:: console 

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

readiness_scripts
=================

Script for MEG analysis of the readiness project

This file will include a description of the files and directories and the thougts behind them


# General remarks

## Badchannels (directory)
- this will include a csv file for each subject with the fro the badchannels to be used in the maxfilter script.

- these file are made with **saveBadChans.py**, which extracts the channel names that are marked as bad the corresponding fif-file

# my\_configs.py
- this file has general purpose settings, e.g. paths to data directory.
- this file can be used to import settings into python scripts, 
    - from my\_configs.py import *

# Preprocessing 
## Preprocessing the raw data
- **maxfilter_function.py**: 
    a function to call the maxfilter for a subject
    - missing: able to select conditions
- **find\_fifs.txt**
    - the find/grep commands to make symbolic-links from fifs in raw to scratch

## Preprocessing the maxfiltered data
- **preproc_func.m**
    - uses Fieldtrip to:
        - Segment data, from -3.5 to 0.5 related to button press.
        - Low-pass filter @ 128Hz
        - Band-pass filter @ 49 & 51, 99, 101
        - Downsample to 256Hz
- **auto\_artifact\_remove.m**
    - uses Fieldtrip to automatically remove trials based on muscle and squid jumps
- **ica\_process.m**
     - uses Fieldtrip to:
        - reduce with PCA to 64 dimensions
        - find ICA components

readiness_scripts
=================

script for MEG analysis of the readiness project

This file will include a desciption of the files and directories and the thougts behind them

- Badchannels
  - this will include a csv file for each subject with the fro teh badchannels to be used in the maxfilter script.

- Preprocessing 
  - maxfilter_function.py: 
    a function to call the maxfilter for a subject
    - missing: able to select conditions
  - find_fifs.txt
    - the find/grep commands to make symbolic-links from fifs in raw to scratchs    


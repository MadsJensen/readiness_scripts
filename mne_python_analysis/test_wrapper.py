#-*- coding: utf-8 -*-

import os

#### ISIS PATHS ####
# setup subjects dir 
os.environ["SUBJECTS_DIR"] = "/projects/MINDLAB2011_24-MEG-readiness/scratch/mri"
# change to the dir  with the pythoon functions# change to the dir  with the pythoon functions
os.chdir("/projects/MINDLAB2011_24-MEG-readiness/scripts/mne_python_analysis")
from preprocessing_function_ver_4 import preprocessing_raw
# change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch/')

##### on wintermute and mounted paths ####
#data_path = "/home/mje/mnt/scratch/"
#subjects_dir = "/home/mje/mnt/scratch/mri/"
#os.environ["SUBJECTS_DIR"] = subjects_dir
## change to the dir  with the pythoon functions# change to the dir  with the pythoon functions

# change data files dir
#os.chdir(data_path)


subs = [11]
sessions = ["classic", "plan"]

os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch/mne_analysis_5')
for sub in subs:
    for session in sessions:
        preprocessing_raw(sub, session)




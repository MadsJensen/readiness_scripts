# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:53:48 2014

@author: mje
"""

import mne
#from mne.minimum_norm import apply_inverse, read_inverse_operator
import os
import pylab as plt
import numpy as np


### on isis paths ####
data_path = "/home/mje/Projects/MEG_libet/mvpa_test"
subjects_dir = "/projects/MINDLAB2011_24-MEG-readiness/scratch/mri/"
os.environ["SUBJECTS_DIR"] = "/projects/MINDLAB2011_24-MEG-readiness/scratch/mri"
# change to the dir  with the pythoon functions# change to the dir  with the pythoon functions
os.chdir("/projects/MINDLAB2011_24-MEG-readiness/scripts/mne_python_analysis")
# change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch/mne_analysis_5')


#### on wintermute and mounted paths ####
#data_path = "/home/mje/mnt/scratch/"
#subjects_dir = "/home/mje/mnt/scratch/mri/"
#os.environ["SUBJECTS_DIR"] = subjects_dir
## change to the dir  with the pythoon functions# change to the dir  with the pythoon functions

# change data files dir
#os.chdir(data_path)



subs =[2,3,4,7,8,9,10,12,13,14,15,16]
#subs = [2]


ts_cls = np.empty([len(subs), 200])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_classic_dSPM_inverse" % subs[j])
#    src = mne.read_source_spaces("sub_%d_classic-src.fif" % subs[j])
    forward =\
        mne.read_forward_solution(
        "sub_%d_classic-tsss-mc-autobad_ver_4-fwd.fif" % subs[j])
    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' 
                            %subs[j])
    precentral_lh = mne.labels_from_parc("fs_sub_%d" %subs[j], parc="aparc", 
                                     subjects_dir = subjects_dir,
                                     regexp="precuneus-lh")[0][0]
    
    stc.crop(-3, -2)
    stc.resample(200)
    
    ts_lh = stc.extract_label_time_course(precentral_lh, forward["src"], 
                                              mode="mean")    
                          
    ts_cls[j,: ] = ts_lh

ts_pln = np.empty([len(subs), 200])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_plan_dSPM_inverse" % subs[j])
    forward =\
        mne.read_forward_solution(
        "sub_%d_plan-tsss-mc-autobad_ver_4-fwd.fif" % subs[j])
    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' 
                            %subs[j])
    precentral_lh = mne.labels_from_parc("fs_sub_%d" %subs[j], parc="aparc", 
                                     subjects_dir = subjects_dir,
                                     regexp="precuneus-lh")[0][0]
    
    stc.crop(-3, -2)    
    stc.resample(200)
    
    ts_lh = stc.extract_label_time_course(precentral_lh,forward["src"], 
                                              mode="mean")    
    
    ts_pln[j] = ts_lh
    
    
plt.figure()
plt.plot(stc.times, ts_cls.mean(axis=0).T, 'b')
plt.plot(stc.times, ts_pln.mean(axis=0).T, 'g')



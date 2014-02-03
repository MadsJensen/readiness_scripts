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

data_path = "/home/mje/Projects/MEG_libet/mvpa_test"
subjects_dir = "/home/mje/Projects/MEG_libet/mne_p_test/"
subject = os.environ['SUBJECT'] = subjects_dir + '/fs_sub_2'
os.environ['SUBJECTS_DIR'] = subjects_dir

subs =[2]


ts_cls = np.empty([12, 3301])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d__dSPM_inverse" % subs[j])
    src = mne.read_source_spaces("sub_%d_classic-src.fif" % subs[j])
    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' %subs[j])
    
    stc.crop(-3.3, 0)    
    
    ts_lh_BA6 = stc.extract_label_time_course(lh_BA6, src, 
                                              mode="mean_flip")    


ts_pln = np.empty([12, 3301])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_plan_dSPM_inverse" % subs[j])
    src = mne.read_source_spaces("sub_%d_plan-src.fif" % subs[j])
    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' %subs[j])
    
    stc.crop(-3.3, 0)    
    
    ts_lh_BA6 = stc.extract_label_time_course(lh_BA6, src, 
                                              mode="mean_flip")    
    
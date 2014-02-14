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

from scipy import stats

### on isis paths ####
data_path = "/home/mje/Projects/MEG_libet/mvpa_test"
subjects_dir = "/projects/MINDLAB2011_24-MEG-readiness/scratch/mri/"
os.environ["SUBJECTS_DIR"] = "/projects/MINDLAB2011_24-MEG-readiness/scratch/mri"
# change to the dir  with the pythoon functions# change to the dir  with the pythoon functions
os.chdir("/projects/MINDLAB2011_24-MEG-readiness/scripts/mne_python_analysis")
# change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch/mne_analysis_5')


### on wintermute and mounted paths ####
#data_path = "/home/mje/mnt/scratch/"
#subjects_dir = "/home/mje/mnt/scratch/mri/"
#os.environ["SUBJECTS_DIR"] = subjects_dir
# change to the dir  with the pythoon functions# change to the dir  with the pythoon functions

# change data files dir
#os.chdir(data_path + "mne_analysis_5")



subs =[2,3,4,7,8,9,10,12,13,14,15,16]



ts_cls = np.empty([len(subs), 401])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_classic_MNE_-275_-235_inverse" % subs[j])
    forward =\
        mne.read_forward_solution(
        "sub_%d_plan-tsss-mc-autobad_ver_4-fwd.fif" % subs[j])
#    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' 
#                            %subs[j])
    precentral_lh = mne.labels_from_parc("fs_sub_%d" %subs[j], parc="aparc", 
                                     subjects_dir = subjects_dir,
                                     regexp="precuneus-lh")[0][0]
    ts_lh = stc.extract_label_time_course(precentral_lh,forward["src"], 
                                              mode="mean")    
    
    ts_cls[j] = ts_lh



ts_pln = np.empty([len(subs), 401])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_plan_MNE_-275_-235_inverse" % subs[j])
    forward =\
        mne.read_forward_solution(
        "sub_%d_plan-tsss-mc-autobad_ver_4-fwd.fif" % subs[j])
#    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' 
#                            %subs[j])
    precentral_lh = mne.labels_from_parc("fs_sub_%d" %subs[j], parc="aparc", 
                                     subjects_dir = subjects_dir,
                                     regexp="precuneus-lh")[0][0]

    ts_lh = stc.extract_label_time_course(precentral_lh,forward["src"], 
                                              mode="mean")    
    
    ts_pln[j] = ts_lh

plt.figure()
plt.plot(stc.times, ts_cls.mean(axis=0).T, 'b')
plt.plot(stc.times, ts_pln.mean(axis=0).T, 'g')

plt.figure()
plt.plot(ts_cls.T, 'b')
plt.plot(ts_pln.T, 'g')

d1 = ts_cls.max(1)
d2 = ts_pln.max(1)
#
#plt.figure()
#plt.boxplot([d1, d2])

print stats.ttest_rel(d1 ,d2)


foobar_ts = np.empty([len(subs), 1])
ts_cls_05_0 = np.empty([len(subs), 400])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_classic_MNE_inverse" % subs[j])
    forward =\
        mne.read_forward_solution(
        "sub_%d_plan-tsss-mc-autobad_ver_4-fwd.fif" % subs[j])
    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' 
                            %subs[j])
#    precentral_lh = mne.labels_from_parc("fs_sub_%d" %subs[j], parc="aparc", 
#                                     subjects_dir = subjects_dir,
#                                     regexp="precentral-lh")[0][0]
    stc.crop(-2.75, -2.35)

    ts_lh = stc.extract_label_time_course(lh_BA6,forward["src"], 
                                              mode="mean")    
    
    ts_cls_05_0[j] = ts_lh
    tmp = stc.in_label(lh_BA6)
    tmp2 = tmp.data
    foobar_ts[j] = tmp2.max()

foobar_ts2 = np.empty([len(subs), 1])
ts_pln_05_0 = np.empty([len(subs), 400])
for j in range(len(subs)):
    stc = mne.read_source_estimate("sub_%d_plan_MNE_inverse" % subs[j])
    forward =\
        mne.read_forward_solution(
        "sub_%d_plan-tsss-mc-autobad_ver_4-fwd.fif" % subs[j])
    lh_BA6 = mne.read_label(subjects_dir + 'fs_sub_%d/label/lh.BA6.label' 
                            %subs[j])
#    precentral_lh = mne.labels_from_parc("fs_sub_%d" %subs[j], parc="aparc", 
#                                     subjects_dir = subjects_dir,
#                                     regexp="precentral-lh")[0][0]
    stc.crop(-2.75, -2.35)    
    ts_lh = stc.extract_label_time_course(lh_BA6,forward["src"], 
                                              mode="mean")    
    ts_pln_05_0[j] = ts_lh
    
    tmp = stc.in_label(lh_BA6)
    tmp2 = tmp.data
    foobar_ts2[j] = tmp2.max()

plt.figure()
plt.plot(stc.times, ts_cls_05_0.mean(axis=0).T, 'b')
plt.plot(stc.times, ts_pln_05_0.mean(axis=0).T, 'g')

#plt.figure()
#plt.plot(ts_cls.T, 'b')
#plt.plot(ts_pln.T, 'g')

d1 = ts_cls_05_0.max(1)
d2 = ts_pln_05_0.max(1)
#
#plt.figure()
#plt.boxplot([d1, d2])


print stats.ttest_rel(d1 ,d2)



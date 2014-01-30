# -*- coding: utf-8 -*-
"""
This file contain project specific settings.
E.g. directory paths, baseline times etc.


Created on Fri Jun 14 13:21:30 2013

@author: mje
"""


n_jobs = 6 # number of processers that mne & scikit-learn can use
# Epoch definitions
tmin, tmax, event_id = -3.5, 0.5, 1
# baseline time
baseline = (-3.5, -3.2)
# filesto reject
reject = dict(grad=4000e-13)
        #eog=150e-6)
    #(mag=4e-12) 

picks = mne.fiff.pick_types(raw_plan.info, meg=True, eeg=False, eog=False, stim=False, exclude='bads')
picks_mag = mne.fiff.pick_types(raw_plan.info, meg='mag', eeg=False, eog=False, stim=False, exclude='bads')
picks_grad = mne.fiff.pick_types(raw_plan.info, meg='grad', eeg=False, eog=False, stim=False, exclude='bads')

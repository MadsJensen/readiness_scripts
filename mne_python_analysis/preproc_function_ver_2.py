# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:33:30 2013

@author: mje
"""

# imports
import mne
from mne.preprocessing.ica import ICA
from mne import fiff
import numpy as np

# Variables

n_jobs = 8  # number of processers that mne & scikit-learn can use

# Epoch definitions
tmin, tmax, event_id = -3.5, 0.5, 1
# baseline time
baseline = (-3.5, -3.2)
# filesto reject

# events to get
event_id = dict(press=1)


def preproc_function(sub_id, session):
    """ 
    This function preprocesse data

    """

    # SETUP AND LOAD FILES ####
    # name with subject id & session name
    fname = "sub_%d_%s" % (sub_id, session)

    # load the raw fif
    print 'Loading raw file'
    raw = fiff.Raw(fname + "_tsss_mc.fif", preload=True)

    picks = mne.fiff.pick_types(raw.info, meg=True, eeg=False, eog=False,
                                stim=False, exclude='bads')

    print 'Computing Covariance matrix'
    cov = mne.compute_raw_data_covariance(raw, picks=picks, reject=None)

    # FILTER ####
    # filter raw, lp 128, bp at 50 & 100
    print 'Low pass filter'
    raw.filter(None, 128, n_jobs=n_jobs, verbose=True)
    print 'Band stop filter'
    raw.notch_filter(np.arange(50, 101, 50), n_jobs=n_jobs, verbose=True)

    # EPOCHS ####
    events = mne.find_events(raw, stim_channel="STI101")
    events_classic = []
    events_interupt = []
    for i in range(len(events)):
        if i > 0:
            if events[i, 2] == 1 and events[i - 1, 2] == 1:
                events_classic.append(i)
            elif events[i, 2] == 1 and events[i - 1, 2] == 2:
                events_interupt.append(i)
        elif i == 0:
            if events[i, 2] == 1:
                events_classic.append(i)

    picks = mne.fiff.pick_types(raw.info, meg='grad', eeg=False, eog=True,
                                emg=True, stim=False, exclude='bads')

    # reject = dict(eog=150e-6)
    epochs = mne.Epochs(raw, events[events_classic], event_id, tmin, tmax,
                        proj=True, picks=picks, baseline=baseline,
                        preload=True, reject=None)
    
    #### ICA ####
    ica = ICA(n_components=0.90, n_pca_components=64, max_pca_components=100,
              noise_cov=None, random_state=0)
    ica.decompose_epochs(epochs)
    sources = ica.get_sources_epochs(epochs, concatenate=True)
    
    # plot first epoch
    times = epochs.times 
    
    # As we have an EOG channel, we can use it to detect the source.
    eog_scores_1 = ica.find_sources_epochs(epochs, target='EOG001',
                                         score_func='pearsonr')
    eog_scores_2 = ica.find_sources_epochs(epochs, target='EOG002',
                                         score_func='pearsonr')
    
    # get maximum correlation index for EOG
    eog_source_idx_1 = np.abs(eog_scores_1).argmax()
    eog_source_idx_2 = np.abs(eog_scores_2).argmax()
    
    # compute times for concatenated epochs
    times = np.linspace(times[0], times[-1] * len(epochs), sources.shape[1])

    ica.exclude += [eog_source_idx_1, eog_source_idx_2]
    
    # Restore sensor space data
    epochs_ica = ica.pick_sources_epochs(epochs)

    # SAVE FILES ####
    raw.save(fname + '_tsss_mc_preproc.fif', overwrite=True)
    cov.save((fname + '_tsss_mc_cov.fif'))
    epochs_ica.save(fname + '_tsss_mc_epochsi_ica.fif')

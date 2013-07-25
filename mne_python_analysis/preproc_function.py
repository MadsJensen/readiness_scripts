# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 10:33:30 2013

@author: mje
"""

# imports
import mne
from mne.preprocessing.ica import ICA
from scipy.stats import pearsonr
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


def preproc_funcion(subId, session):
    """ 
    This function preprocesse data

    """
    # name with subject id & session name
    fname = "sub_%d_%s" % (subId, session)

    # load the raw fif
    print 'Loading raw file'
    raw = fiff.Raw(fname + "_tsss_mc.fif", preload=True)

    picks = mne.fiff.pick_types(raw.info, meg=True, eeg=False, eog=False,
                                stim=False, exclude='bads')

    print 'Computing Covariance matrix'
    cov = mne.compute_raw_data_covariance(raw, picks=picks, reject=None)

    # filter raw, lp 128, bp at 50 & 100
    print 'Low pass filter'
    raw.filter(None, 128, n_jobs=n_jobs, verbose=True)
    print 'band stop filter'
    raw.notch_filter(np.arange(50, 101, 50), n_jobs=n_jobs, verbose=True)

    # run ICA
    print 'Run ICA'
    ica = ICA(n_components=0.90, n_pca_components=64, max_pca_components=100,
              noise_cov=None, random_state=0)

    start, stop = None, None

    # decompose sources for raw data
    ica.decompose_raw(raw, start=start, stop=stop, picks=picks)
    corr = lambda x, y: np.array([pearsonr(a, y.ravel()) for a in x])[:, 0]
    eog_scores_1 = ica.find_sources_raw(raw, target='EOG001', score_func=corr)
    eog_scores_2 = ica.find_sources_raw(raw, target='EOG002', score_func=corr)

    # get maximum correlation index for EOG
    eog_source_idx_1 = np.abs(eog_scores_1).argmax()
    eog_source_idx_2 = np.abs(eog_scores_2).argmax()

    # We now add the eog artifacts to the ica.exclusion list
    ica.exclude += [eog_source_idx_1, eog_source_idx_2]

    # Restore sensor space data
    raw_ica = ica.pick_sources_raw(raw, include=None)

    events = mne.find_events(raw_ica)
    events_classic = []
    events_interupt = []
    for i in range(len(events)):
        if i > 0:
            if events[i, 2] == 1 and events[i - 1, 2] == 1:
                events_classic.append(i)
            elif events[i, 2] == 1 and events[i - 1, 2] == 2:
                events_interupt.append(i)

    picks = mne.fiff.pick_types(raw_ica.info, meg='grad', eeg=False, eog=False,
                                stim=False, exclude='bads')

    reject = dict(grad=4000e-13)
    epochs = mne.Epochs(raw, events[events_classic], event_id, tmin, tmax,
                        proj=True, picks=picks, baseline=baseline,
                        preload=False, reject=reject)

    raw_ica.save(fname + '_tsss_mc_preproc_ica.fif', overwrite=True)
    cov.save((fname + '_tsss_mc_cov.fif'))
    epochs.save(fname + '_tsss_mc_epochs.fif')

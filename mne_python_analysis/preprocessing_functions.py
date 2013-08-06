# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:00:46 2013

@author: mje
"""

import os
import logging
import mne
from mne.minimum_norm import make_inverse_operator, apply_inverse, \
    write_inverse_operator
from mne.preprocessing.ica import ICA
from scipy.stats import pearsonr
from mne import fiff
import numpy as np


n_jobs = 8  # number of processers that mne & scikit-learn can use

# Epoch definitions
tmin, tmax, event_id = -3.5, 0.5, 1
# baseline time
baseline = (-3.5, -3.2)
# filesto reject

# events to get
event_id = dict(press=1)

logger = logging.getLogger('mne')


def mne_forward_wrapper(sub_id,
                        sessions=["classic", "plan", "interupt"],
                        ico=4, mindist=5,  spacing=5,
                        datapath='/projects/MINDLAB2011_24-MEG-readiness/scratch',
                        MRIpath='/projects/MINDLAB2011_24-MEG-readiness/scratch/mri'):
    """ calls mne_setup_forward_model
    """
    # Run mne_setup_forward_model
    fname = "fs_sub_%d" % sub_id

    cmd = ("mne_setup_forward_model --subject %s --surf --homog --ico %d "
           % (fname, ico))

    st = os.system(cmd)

    # run mne_do_forward_model
    bem = MRIpath + "/%s/bem/%s-5120-bem-sol-fif" % (fname, fname)
    src = MRIpath + "/%s/bem/%s-5-src.fif" % (fname, fname)

    for session in sessions:

        meas = datapath + "/sub_%d_%s_tsss_mc.fif" % (sub_id, session)
        fwd = datapath + "/sub_%d_%s_tsss_mc_fwd.fif" % (sub_id, session)

        cmd = ("mne_do_forward_solution \
                --overwrite \
                --subject %s\
                --mindist %d \
                --spacing %d \
                --megonly \
                --bem %s \
                --src %s \
                --meas %s \
                --fwd %s"
               % (fname, mindist, spacing, bem, src, meas, fwd))

        logger.info('Running mne_do_forward_model: %s ' % cmd)
        st = os.system(cmd)
        if st != 0:
            raise RuntimeError("mne_do_forward_model returned" +
                               "non-zero exit status %d" % st)
        logger.info('[done]')


def inverse_function(sub_id, session):
    """ Will calculate the inverse model based dSPM
    """
    data_path = "/projects/MINDLAB2011_24-MEG-readiness/scratch/"
    fname = "sub_%d_%s_tsss_mc" % (sub_id, session)
    fname_epochs = data_path + fname + "_epochs.fif"
    fname_fwd_meg = data_path + fname + "_fwd.fif"
    fname_cov = data_path + fname + "_cov.fif"
    fname_inv = data_path + fname + "_inv.fif"
    fname_stcs = fname + "_mne_dSPM_inverse"

    epochs = mne.read_epochs(fname_epochs)
    evoked = epochs.average()

    snr = 3.0
    lambda2 = 1.0 / snr ** 2

    # Load data
    forward_meg = mne.read_forward_solution(fname_fwd_meg, surf_ori=True)
    noise_cov = mne.read_cov(fname_cov)

    # regularize noise covariance
    noise_cov = mne.cov.regularize(noise_cov, evoked.info,
                                   mag=0.05, grad=0.05, eeg=0.1, proj=True)

    # Restrict forward solution as necessary for MEG
    forward_meg = mne.fiff.pick_types_forward(forward_meg, meg=True, eeg=False)

    # make an M/EEG, MEG-only, and EEG-only inverse operators
    info = evoked.info
    inverse_operator_meg = make_inverse_operator(info, forward_meg, noise_cov,
                                                 loose=0.2, depth=0.8)

    write_inverse_operator(fname_inv, inverse_operator_meg)

    # Compute inverse solution
    stcs = apply_inverse(evoked, inverse_operator_meg, lambda2, "dSPM",
                         pick_normal=False)

    # Save result in stc files
    stcs.save(fname_stcs)


def preprocess_raw(sub_id, session):
    """ This function preprocessess data
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
    raw.filter(None, 128, n_jobs=n_jobs, verbose=True)

    steps = np.arange(50, 151, 50)
    print 'Band stop filter at %s' % steps
    raw.notch_filter(steps, n_jobs=n_jobs, verbose=True)

    # ICA ####
    print 'Run ICA'
    ica = ICA(n_components=0.90, n_pca_components=64, max_pca_components=100,
              noise_cov=None, random_state=0)

    start, stop = None, None

    # decompose sources for raw data
    ica.decompose_raw(raw, start=start, stop=stop, picks=picks)

    corr = lambda x, y: np.array([pearsonr(a, y.ravel()) for a in x])[:, 0]

    eog_scores_1 = ica.find_sources_raw(raw, target='EOG001',
                                        score_func=corr)
    eog_scores_2 = ica.find_sources_raw(raw, target='EOG002',
                                        score_func=corr)

    # get maximum correlation index for EOG
    eog_source_idx_1 = np.abs(eog_scores_1).argmax()
    eog_source_idx_2 = np.abs(eog_scores_2).argmax()

    # We now add the eog artifacts to the ica.exclusion list
    if eog_source_idx_1 ==  eog_source_idx_2:
        ica.exclude = eog_source_idx_1
    elif eog_source_idx_1 !=  eog_source_idx_2:
        ica.exclude = [eog_source_idx_1, eog_source_idx_2]

    print eog_source_idx_1, eog_source_idx_2
    print ica.exclude

    # Restore sensor space data
    raw_ica = ica.pick_sources_raw(raw, include=None)

    # EPOCHS ####
    events = mne.find_events(raw_ica, stim_channel="STI101")
    events_classic = []
    events_interupt = []
    for i in range(len(events)):
        if i > 0:
            if events[i, 2] == 1 and events[i - 1, 2] == 1:
                events_classic.append(i)
            elif events[i, 2] == 1 and events[i - 1, 2] == 2:
                events_interupt.append(i)

    picks = mne.fiff.pick_types(raw_ica.info, meg='grad', eeg=False, eog=True,
                                emg=True, stim=False, exclude='bads')

    reject = dict(grad=4000e-13)
    epochs = mne.Epochs(raw_ica, events[events_classic], event_id, tmin, tmax,
                        proj=True, picks=picks, baseline=baseline,
                        preload=False, reject=reject)

    # SAVE FILES ####
    raw_ica.save(fname + '_tsss_mc_preproc_ica.fif', overwrite=True)
    cov.save((fname + '_tsss_mc_cov.fif'))
    epochs.save(fname + '_tsss_mc_epochs.fif')

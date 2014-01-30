# -*- coding: utf-8 -*-
"""
Function to preprocess raw fif data, see function doc string for details.
Written by Mads Jensen (mje.mads@gmail.com)

Last edited 28-jan-2014

"""

import numpy as np

import mne
from mne.preprocessing import ICA
from mne.minimum_norm import make_inverse_operator, apply_inverse

# directories
subjects_dir = "/projects/MINDLAB2011_24-MEG-readiness/mri"
data_path = "/projects/MINDLAB2011_24-MEG-readiness/scratch"

#epoch variables
tmin, tmax = -3.5, 0.5
baseline = (-3.5, -3.3)  # baseline time
reject = dict(mag=4e-12, grad=4000e-13)


# inversion variables
snr = 3.0
lambda2 = 1.0 / snr ** 2


def preprocessing_raw(sub_id, session):
    """
    #########################################################################
    Preprocessing function for raw fif data,

    - Data is lowpass filtered at 48Hz
    - Raw is epoched from -3500ms to 500ms after button press
    - Epochs are rejected by MAG & GRAD channels
    - ICA is computed and the component correlating with the EOG channel
        is automatically removed.
    - Noise cov is calculated
    - forward model is computed
    - inverse solution with dSPM and MNE is computed.

    #########################################################################
    """
    #########################################################################
    # Load and filter data, set up epochs
    #########################################################################
    fs_sub = "fs_sub_%d" % sub_id

    # load raw fif file
    raw = mne.fiff.Raw(data_path +
                       "sub_%d_%s_tsss_mc.fif" % (sub_id, session),
                       preload=True)

    picks = mne.fiff.pick_types(raw.info, meg=True, eog=True, emg=True,
                                exclude='bads')
    raw.filter(0, 48, method='iir', n_jobs=8)

    events = mne.find_events(raw, stim_channel='STI101')
    event_ids = {"press": 1}

    epochs = mne.Epochs(raw, events, event_ids, tmin, tmax,
                        picks=picks, baseline=baseline, preload=True,
                        reject=reject)

    ########################################################################
    # ICA
    ########################################################################
    # Fit ICA, find and remove major artefacts
    ica = ICA(n_components=0.90, n_pca_components=64,
              max_pca_components=100,
              noise_cov=None)

    ica.decompose_epochs(epochs, decim=2)

    eog_scores_1 = ica.find_sources_epochs(epochs, target="EOG001",
                                           score_func="pearsonr")
    eog_scores_2 = ica.find_sources_epochs(epochs, target="EOG002",
                                           score_func="pearsonr")

    # get maximum correlation index for EOG
    eog_source_idx_1 = np.abs(eog_scores_1).argmax()
    eog_source_idx_2 = np.abs(eog_scores_2).argmax()

    # select ICA sources and reconstruct MEG signals, compute clean ERFs
    # Add detected artefact sources to exclusion list
    # We now add the eog artefacts to the ica.exclusion list
    if eog_source_idx_1 == eog_source_idx_2:
        ica.exclude += [eog_source_idx_1]
    elif eog_source_idx_1 != eog_source_idx_2:
        ica.exclude += [eog_source_idx_1, eog_source_idx_2]

    # Restore sensor space data
    epochs_ica = ica.pick_sources_epochs(epochs)
    epochs_ica.save("sub_%d_%s_epochs.fif" % (sub_id, session))

    evoked = epochs_ica.average()
    evoked.save("sub_%d_%s-evk.fif" % (sub_id, session))

    ########################################################################
    # estimate noise covariance
    ########################################################################
    noise_cov = mne.compute_covariance(epochs.crop(-3.5, -3.3,
                                                   copy=True))
    # save noise cov
    noise_cov.save("sub_%d_%s-cov.fif" % (sub_id, session))

    ########################################################################
    # Compute forward model
    ########################################################################
    # Make source space
    src = mne.setup_source_space(fs_sub, spacing='ico4',
                                 subjects_dir=subjects_dir,
                                 overwrite=True)
    src.save("sub_%d_%s-src.fif" % (sub_id, session))

    mri = "sub_%d_%s-trans.fif" % (sub_id, session)
    bem = fs_sub + "/bem/" + fs_sub + "-5120-bem-sol.fif"
    forward = mne.make_forward_solution(epochs_ica.info, mri=mri,
                                        src=src, bem=bem)
    forward = mne.convert_forward_solution(forward, surf_ori=True)

    mne.write_forward_solution("sub_%d_%s-fwd.fif" % (sub_id, session),
                               forward, overwrite=True)

    ########################################################################
    # Compute inverse solution
    ########################################################################
    method = 'dSPM'

    inverse_operator = make_inverse_operator(evoked.info,
                                             forward, noise_cov,
                                             loose=0.2, depth=0.8)

    # Compute inverse solution on contrast
    stc = apply_inverse(evoked, inverse_operator, lambda2, method,
                        pick_normal=None)
    stc.save("sub_%d_%s_%s_inverse" % (sub_id, session, method))

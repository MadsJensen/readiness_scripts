# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 10:23:36 2013

@author: mje
"""

import numpy as np
import mne
from mne.layouts.layout import _merge_grad_data
from mne.baseline import rescale


subjects_dir = "/projects/MINDLAB2011_24-MEG-readiness/scratch/mri"


def combine_grads(epochs, baseline=(-3.5, -3.2)):
    """Combines data from Epochs into a RMS data structure
    """

    data_picks = mne.fiff.pick_types(epochs.info, meg='grad', exclude='bads')
    data = epochs.get_data()[:, data_picks, :]
    data_rms = np.empty([data.shape[0], data.shape[1]/2, data.shape[2]])

    for i in range(len(data)):
        data_rms[i, :, :] = _merge_grad_data(data[i, :, :])

    if baseline is not None:
        data_rms = rescale(data_rms, times=epochs.times,
                           baseline=(-3.5, -3.2), mode="mean")
    return data_rms


def global_RMS(sub, session, baseline=500, selection="Vertex"):
    """ make global RMS
        baseline is in indexes
    """

    f_load = "sub_%d_%s_tsss_mc_epochs.fif" % (sub, session)
    epochs = mne.read_epochs(f_load)

    if selection is not None:
        selection = mne.viz._clean_names(mne.read_selection(selection))
        data_picks = mne.epochs.pick_types(epochs.info, meg='grad',
                                           exclude='bads', selection=None)
    else:
        data_picks = mne.epochs.pick_types(epochs.info, meg='grad',
                                           exclude='bads')

    data = epochs.get_data()[:, data_picks, :]
    data = np.sqrt(np.square(data.mean(axis=0)))
    data = data.mean(axis=0)
    baseline_std = data[:baseline].std().mean()

    grms = data/baseline_std

    return grms


def max_values(sub_id, session, twoi_start, twoi_end, BA, hemi="lh"):
    """ Function return the maximum value for the subject
    as a single value.
    """

    stc = mne.read_source_estimate("sub_%d_%s_MNE_inverse_morph"
                                   % (sub_id, session))
    src =\
        mne.read_source_spaces(subjects_dir +
                               "/fsaverage/bem/fsaverage-7-src.fif")
    label = mne.labels_from_parc("fsaverage", parc="PALS_B12_Brodmann",
                                 subjects_dir=subjects_dir,
                                 regexp="Brodmann.%d-%s"
                                 % (BA, hemi))[0][0]

    stc.crop(twoi_start, twoi_end)

    tc = stc.extract_label_time_course(label, src=src, mode="max")
    return tc.max()


def mean_values(sub_id, session, twoi_start, twoi_end, BA, hemi="lh"):
    """ Function return the maximum value for the subject
    as a single value.
    """

    stc = mne.read_source_estimate("sub_%d_%s_MNE_inverse_morph"
                                   % (sub_id, session))
    src =\
        mne.read_source_spaces(subjects_dir +
                               "/fsaverage/bem/fsaverage-7-src.fif")
    label = mne.labels_from_parc("fsaverage", parc="PALS_B12_Brodmann",
                                 subjects_dir=subjects_dir,
                                 regexp="Brodmann.%d-%s"
                                 % (BA, hemi))[0][0]

    stc.crop(twoi_start, twoi_end)

    tc = stc.extract_label_time_course(label, src=src, mode="max")
    return tc.mean()


def max_values_tc(sub_id, session, twoi_start, twoi_end, BA, hemi="lh"):
    """ Function return the maximum value for the subject
    as a single value.
    """

    stc = mne.read_source_estimate("sub_%d_%s_MNE_inverse_morph"
                                   % (sub_id, session))
    src =\
        mne.read_source_spaces(subjects_dir +
                               "/fsaverage/bem/fsaverage-7-src.fif")
    label = mne.labels_from_parc("fsaverage", parc="PALS_B12_Brodmann",
                                 subjects_dir=subjects_dir,
                                 regexp="Brodmann.%d-%s"
                                 % (BA, hemi))[0][0]

    stc.crop(twoi_start, twoi_end)

    return stc.extract_label_time_course(label, src=src, mode="max")


def time_for_max_value(sub_id, session, twoi_start, twoi_end, BA, hemi="lh"):
    """ Function return the maximum value for the subject
    as a single value.
    """

    stc = mne.read_source_estimate("sub_%d_%s_MNE_inverse_morph"
                                   % (sub_id, session))
    src =\
        mne.read_source_spaces(subjects_dir +
                               "/fsaverage/bem/fsaverage-7-src.fif")
    label = mne.labels_from_parc("fsaverage", parc="PALS_B12_Brodmann",
                                 subjects_dir=subjects_dir,
                                 regexp="Brodmann.%d-%s"
                                 % (BA, hemi))[0][0]

    stc.crop(twoi_start, twoi_end)

    tc = stc.extract_label_time_course(label, src=src, mode="max")

    maxIndex = tc.argmax()
    time_for_max = stc.times[maxIndex]

    return time_for_max

"""
Created on Tue Aug  6 11:43:52 2013

@author: mje
"""

import mne
from mne.minimum_norm import make_inverse_operator, apply_inverse, \
                             write_inverse_operator
#sub_id = 2
#session = "classic"

def inverse_function(sub_id, session):
    data_path = "/projects/MINDLAB2011_24-MEG-readiness/scratch/"
    fname = "sub_%d_%s_tsss_mc" %(sub_id, session)
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
    

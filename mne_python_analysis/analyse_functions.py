# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 10:23:36 2013

@author: mje
"""

import numpy as np
import mne
from mne.layouts.layout import _merge_grad_data
from mne.baseline import rescale


def combine_grads(epochs, baseline=(-3.5, -3.2)):
    """Combines data from Epochs into a RMS data structure
    """    

    data_picks = mne.fiff.pick_types(epochs.info, meg='grad', exclude='bads')
    data = epochs.get_data()[:, data_picks, :]
    data_rms = np.empty([data.shape[0], data.shape[1]/2, data.shape[2]])

    for i in range(len(data)):
        data_rms[i, :, :] = _merge_grad_data(data[i, :, :])
        
    if baseline is not None:
        data_rms = rescale(data_rms, times = epochs.times, 
                baseline = (-3.5, -3.2), mode="mean")

    return data_rms



sessions  = ["plan", "interupt"]
subs = [2]
dummy = 0
X = []

for session in sessions:
    for sub in subs:
    
        f_load = "sub_%d_%s_tsss_mc_epochs.fif" %(sub, session)
        print f_load

        epochs = mne.read_epochs(f_load)        
        evk = epochs.average()
        
        foo = evk.data[:, 500:-500]       
        if dummy == 0:
            X = foo.reshape(-1)
            dummy = 1
        else:
            X = np.vstack([X, foo.reshape(-1)])





def global_RMS(sub, session, baseline=500):
    """ make global RMS 
        baseline is in indexes
    """
    
    f_load = "sub_%d_%s_tsss_mc_epochs.fif" %(sub, session)
    epochs = mne.read_epochs(f_load)
    evoked = epochs.average()
    
    selection = mne.viz._clean_names(mne.read_selection("Vertex"))
    data_picks = mne.epochs.pick_types(epochs.info, meg='grad', exclude='bads', 
                                       selection = selection)
    
    data = evoked.data[data_picks, :]
    data = np.sqrt(np.square(data))
    data = data.mean(axis = 0)
    baseline_std = data[:baseline].std().mean()
    
    grms = data/baseline_std
    
    return grms
    








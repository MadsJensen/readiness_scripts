# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:08:40 2013

@author: mje
"""

from mne import fiff
import csv
import mne

def save_bad_chans(sub_id, session):
    """
    function to extract the bad channel number from a fif file and save them as a  
    """
    raw_fname = "sub_" + str(sub_id) + "_%s_raw.fif" % session
    bad_chans_fname = "sub_" + str(sub_id) + "_%s_badChans.csv" % session
    
    raw = fiff.Raw(raw_fname, preload=False)
    bad_chans = raw.info['bads']
    picks = mne.fiff.pick_types(raw.info, meg='grad', eeg=False, eog=False, stim=False, exclude='bads')

    bc_list = []
    for i in range(len(bad_chans)):
        bc_list.append(bad_chans[i][-4:])
    csv_writer = csv.writer(open(bad_chans_fname , 'wb'), delimiter=',').writerow           
    csv_writer(bc_list)                                                      


#    for bc in foo:
#        f.write("%s\n" % bc)


conditions = ['plan', 'classic', 'interupt']
subs = [1,2,3,4,5,6,7,8,9,10]
for condition in conditions:
    for sub in subs:
        save_bad_chans(sub, condition)




conditions = ['plan']
subs = [1]
for condition in conditions:
    for sub in subs:
        print "subs[sub], conditions[condition]"


# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:08:40 2013

@author: mje
"""

from mne import fiff
import csv


def save_bad_chans(sub_id, session):
    """
    function to extract the bad channel number from a fif file and save them as a  
    """
    raw_fname = "sub_" + str(sub_id) + "_%s_raw.fif" % session
    bad_chans_fname = "sub_" + str(sub_id) + "_%s_badChans.csv" % session
    
    raw = fiff.Raw(raw_fname, preload=False)
    bad_chans = raw.info['bads']

    bc_list = [0]
    for i in range(len(bad_chans)):
        bc_list.append(bad_chans[i][-4:])
    csv_writer = csv.writer(open(bad_chans_fname , 'wb'), delimiter=',').writerow           
    csv_writer(bc_list)                                                      


#    for bc in foo:
#        f.write("%s\n" % bc)


conditions = ['plan', 'classic', 'interupt']
subs = [2,3]
for condition in conditions:
    for sub in subs:
        save_bad_chans(sub, condition)

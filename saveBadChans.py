# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:08:40 2013

@author: mje
"""

from mne import fiff


def saveBadChns(sub_id, session):
    raw_fname = "sub_" + str(sub_id) + "_%s_raw.fif" % session
    badChns_fname = "sub_" + str(sub_id) + "_%s_badChans.txt" % session
    f = open(badChns_fname, 'w')

    raw = fiff.Raw(raw_fname, preload=False)
    badChans = raw.info['bads']
    for bc in badChans:
        f.write("%s\n" % bc)

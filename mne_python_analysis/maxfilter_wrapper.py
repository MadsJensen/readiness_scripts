# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:58:16 2013

@author: mje
"""

from mne.preprocessing.maxfilter import apply_maxfilter
import os

# change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch')

#subs = [3, 4, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
subs = [2]

#
sessions = ["classic", "plan"]
for sub in subs:
    for session in sessions:

        # file and log names
        in_name = "sub_%d_%s-raw.fif" % (sub, session)
        out_name = "sub_%d_%s-tsss-mc-autobad_ver_4.fif" % (sub, session)
        tsss_mc_log = "sub_%d_%s-tsss-mc-autobad_ver_4.log" % (sub, session)
        headpos_log = "sub_%d_%s-headpos_ver_4.log" % (sub, session)

        #call to maxfilter
        apply_maxfilter(in_fname=in_name,
                        out_fname=out_name,
                        frame='head',
#                        origin= "0 0 40",
                        autobad="on",
                        st=True,
                        st_buflen=30,
                        st_corr=0.95,
                        mv_comp=True,
                        mv_hp=headpos_log,
                        cal='/projects/MINDLAB2011_24-MEG-readiness/misc/sss_cal_Mar11-May13.dat',
                        ctc='/projects/MINDLAB2011_24-MEG-readiness/misc/ct_sparse_Mar11-May13.fif',
                        overwrite=True,
                        mx_args=' -v | tee %s' % tsss_mc_log,
                        )




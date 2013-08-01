

import csv
from mne.preprocessing.maxfilter_mj import apply_maxfilter
#### Select (sub, condition)s and subjects numbers to maxfilter

conditions = ["plan"]
subs = [2]


cal = "/projects/MINDLAB2011_24-MEG-readiness/misc/sss_cal_Mar11-May13.dat "
ctc  = "/projects/MINDLAB2011_24-MEG-readiness/misc/ct_sparse_Mar11-May13.fif "

for condition in conditions:
    for sub in subs:
        raw_fname = "sub_%d_%s_raw.fif" % (sub, condition)
        tsss_fname = "sub_%d_%s_tsss_mc.fif" % (sub, condition)
        tsss_logname = "sub_%d_%s_tsss_mc.log" % (sub, condition)
        trans_fname = "sub_%d_%s_tsss_mc_trans.fif" % (sub, condition)
        trans_logname = "sub_%d_%s_tsss_mc_trans.log" % (sub, condition)
        headpos_logname = "sub_%d_%s_headpos.txt " % (sub, condition)
        

        badchannel_path = "/projects/MINDLAB2011_24-MEG-readiness/misc/Badchannels/"
        badchannel_filename = 'sub_%d_%s_badChans.csv' % (sub, condition)
        bcFname = badchannel_path + badchannel_filename
        badchannels = list(csv.reader(open(bcFname)))

        apply_maxfilter(raw_fname, 
                tsss_fname,
                origin=None,
                frame='head',
                bad='%s' %badchannels,
                autobad='off',
                skip=None,
                force=False,
                st=True, 
                st_buflen=10.,
                st_corr=0.980 ,
                mv_trans=None,
                mv_comp=True,
                mv_headpos=False,
                mv_hp='%s' % headpos_logname, 
                mv_hpistep=None,
                mv_hpisubt=None,
                mv_hpicons=True,
                linefreq=None,
                mx_args='-v | tee %s ' % tsss_logname,
                overwrite=True,
                verbose=True,
                cal=cal,
                ctc=ctc,
                )

     

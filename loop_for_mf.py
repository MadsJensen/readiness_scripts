
from mne.preprocessing import maxfilter_mj

#### Select conditions and subjects numbers to maxfilter

conditions = ["plan"]
subs = [2]


cal = "/projects/MINDLAB2011_24-MEG-readiness/misc/sss_cal_Mar11-May13.dat "
ctc  = "/projects/MINDLAB2011_24-MEG-readiness/misc/ct_sparse_Mar11-May13.fif "

for condition in conditions:
    for sub in subs:
        raw_fname = "sub_" + str(sub_id) + "_%s_raw.fif" % session
        tsss_fname = "sub_" + str(sub_id) + "_%s_tsss_mc.fif" % session
        tsss_logname = "sub_" + str(sub_id) + "_%s_tsss_mc.log" % session
        trans_fname = "sub_" + str(sub_id) + "_%s_tsss_mc_trans.fif" % session
        trans_logname = "sub_" + str(sub_id) + "_%s_tsss_mc_trans.log" % session
        headpos_logname = "sub_" + str(sub_id) + "_%s_headpos.txt" % session

        apply_maxfilter(raw_fname, 
                tsss_fname,
                origin=None 
                frame='device'
                bad=None
                autobad='off'
                skip=None
                force=False
                st=10, 
                st_buflen=16.0
                st_corr=0.96 
                mv_trans=None
                mv_comp=True
                mv_headpos=True
                mv_hp=headpos_logname
                mv_hpistep=None
                mv_hpisubt=None
                mv_hpicons=True
                linefreq=None
                mx_args='| tee %s ' % tsss_logname
                overwrite=True
                verbose=True
                cal=cal
                ctc=ctc
                )

     

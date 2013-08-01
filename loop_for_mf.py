
from mne.preprocessing.maxfilter_mj import apply_maxfilter

#### Select conditions and subjects numbers to maxfilter

conditions = ["plan"]
subs = [2]


cal = "/projects/MINDLAB2011_24-MEG-readiness/misc/sss_cal_Mar11-May13.dat"
ctc  = "/projects/MINDLAB2011_24-MEG-readiness/misc/ct_sparse_Mar11-May13.fif"

for condition in conditions:
    for sub in subs:
        raw_fname = "sub_" + str(sub) + "_%s_raw.fif" % condition
        tsss_fname = "sub_" + str(sub) + "_%s_tsss_mc.fif" % condition
        tsss_logname = "sub_" + str(sub) + "_%s_tsss_mc.log" % condition
        trans_fname = "sub_" + str(sub) + "_%s_tsss_mc_trans.fif" % condition
        trans_logname = "sub_" + str(sub) + "_%s_tsss_mc_trans.log" % condition
        headpos_logname = "sub_" + str(sub) + "_%s_headpos.txt" % condition

        apply_maxfilter(raw_fname, 
                tsss_fname,
                origin=None, 
                frame='head',
                bad=None,
                autobad='off',
                skip=None,
                force=True,
                st=True, 
                st_buflen=16.0,
                st_corr=0.96,
                mv_trans=None,
                mv_comp=True,
                mv_headpos=False,
                mv_hp=True,
                mv_hpistep=None,
                mv_hpisubt=None,
                mv_hpicons=True,
                linefreq=None,
                mx_args='-v | tee %s ' % tsss_logname,
                overwrite=True,
                verbose=True,
                cal=cal,
                ctc=ctc
                )

     

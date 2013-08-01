
from mne.preprocessing.maxfilter_mj import apply_maxfilter

#### Select conditions and subjects numbers to maxfilter

conditions = ["plan"]
subs = [2]


cal = "/projects/MINDLAB2011_24-MEG-readiness/misc/sss_cal_Mar11-May13.dat"
ctc  = "/projects/MINDLAB2011_24-MEG-readiness/misc/ct_sparse_Mar11-May13.fif"

for condition in conditions:
    for sub in subs:
<<<<<<< HEAD
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
=======
        raw_fname = "sub_" + str(sub_id) + "_%s_raw.fif" % session
        tsss_fname = "sub_" + str(sub_id) + "_%s_tsss_mc.fif" % session
        tsss_logname = "sub_" + str(sub_id) + "_%s_tsss_mc.log" % session
        trans_fname = "sub_" + str(sub_id) + "_%s_tsss_mc_trans.fif" % session
        trans_logname = "sub_" + str(sub_id) + "_%s_tsss_mc_trans.log" % session
        headpos_logname = "sub_" + str(sub_id) + "_%s_headpos.txt" % session
        

        badchannel_path = project_path + "/projects/MINDLAB2011_24-MEG-readiness/misc/Badchannels/"
        badchannel_filename = 'sub_' + str(sub_id) + '_%s_badChans.csv' % session
        bcFname = badchannel_path + badchannel_filename
        badchannels = list(csv.reader(open(bcFname)))

        apply_maxfilter(raw_fname, 
                tsss_fname,
                origin=None 
                frame='device'
                bad='%s' %badchannels
                autobad='off'
                skip=None
                force=False
                st=True, 
                st_buflen=10.
                st_corr=0.980 
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
>>>>>>> b112c7194c10d4b919029afc5028d7b7f49a2774
                ctc=ctc
                )

     



import csv

def mfFunction(sub_id, session):
    # Paths
    project_path = "/projects/MINDLAB2011_24-MEG-readiness/"
    badchannel_path = project_path + "scripts/Badchannels/"
<<<<<<< HEAD
=======
    sss_sparse_path = "/projects/MINDLAB2011_24-MEG-readiness/misc/sss_cal_Mar11-May13.dat"
    ctc_path = "/projects/MINDLAB2011_24-MEG-readiness/misc/ct_sparse_Mar11-May13.fif"
>>>>>>> develop
    #
    # file names for planning session
    raw_fname = "sub_" + str(sub_id) + "_%s_raw.fif" % session
    tsss_fname = "sub_" + str(sub_id) + "_%s_tsss_mc.fif" % session
    tsss_logname = "sub_" + str(sub_id) + "_%s_tsss_mc.log" % session
    trans_fname = "sub_" + str(sub_id) + "_%s_tsss_mc_trans.fif" % session
    trans_logname = "sub_" + str(sub_id) + "_%s_tsss_mc_trans.log" % session
    headpos_logname = "sub_" + str(sub_id) + "_%s_headpos.txt" % session
    #
    # setup the badchannels
    badchannel_filename = 'sub_' + str(sub_id) + '_%s_badChans.csv' % session
    bcFname = badchannel_path + badchannel_filename
    badchannels = list(csv.reader(open(bcFname)))
    
    print badchannels
    # badchannels = np.genfromtxt(bcFname, delimiter=
    #
    #  apply maxfilter to correct for bad channels, movement & tsss
<<<<<<< HEAD
    !/neuro/bin/util/maxfilter -f {raw_fname} -o {tsss_fname} -st 10 -movecomp -hp {headpos_logname} -bad {badchannels} -v -force | tee {tsss_logname}    # 
    # apply maxfilter to make the transformation to 0,0,0
    !/neuro/bin/util/maxfilter -f {tsss_fname} -o {trans_fname} -trans default -force -v | tee {trans_logname}
=======
    !/neuro/bin/util/maxfilter -f {raw_fname} -o {tsss_fname} -st 10 -movecomp -hp {headpos_logname} -bad {badchannels} -v -force -cal {sss_sparse_path} -ctc {ctc_path} | tee {tsss_logname}    
    # apply maxfilter to make the transformation to 0,0,0
    !/neuro/bin/util/maxfilter -f {tsss_fname} -o {trans_fname} -frame head -origin 0 0 40 -trans default -force -v --cal {sss_sparse_path} -ctc {ctc_path} | tee {trans_logname}
>>>>>>> develop
    





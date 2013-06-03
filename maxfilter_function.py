
from mne import fiff


def mfFunction(sub_id, session):
    # Paths
    project_path = "/projects/MINDLAB2011_24-MEG-readiness/"
    badchannel_path = project_path + "scripts/Badchannels/"
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
    raw = fiff.Raw(raw_fname, preload=False)
    badChns = raw.info['bads']
    badchannel_filename = 'sub_' + str(sub_id) + '_%s_bc.csv' % session
    bcFname = badchannel_path + badchannel_filename
    badchannels = np.genfromtxt(bcFname, delimiter=',', dtype='int')
    #
    # apply maxfilter to correct for movements and badchannels
    !/neuro/bin/util/maxfilter -f {raw_fname} -o {tsss_fname} -st 10 -movecomp -hp {headpos_logname} -bad {badchannels} -v -force | tee {tsss_logname}
    #
    # apply maxfilter to make the transformation to 0,0,0
    !/neuro/bin/util/maxfilter -f {tsss_fname} -o {trans_fname} -trans default -force -v | tee {trans_logname}

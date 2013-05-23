

def mfFunction(sub_id):
   

    # Paths
    project_path = "/projects/MINDLAB2011_24-MEG-readiness/"
    badchannel_path = project_path + "scripts/Badchannels/"
    
    # file names
    raw_fname = "sub_" + str(sub_id) + "_plan_raw.fif"  
    tsss_fname = "sub_" + str(sub_id) + "_tsss_mc_plan.fif"   
    tsss_logname = "sub_" + str(sub_id) + "_tsss_mc_plan.log" 
    trans_fname = "sub_" + str(sub_id) + "_tsss_mc_trans_plan.fif" 
    trans_logname = "sub_" + str(sub_id) + "_tsss_mc_trans_plan.log" 
    headpos_logname = "sub_" + str(sub_id) + "_headpos_plan.txt"
    
    # setup the badchannels
    badchannel_filename = 'sub_' + str(sub_id) + '_bc_plan.csv'
    bcFname = badchannel_path + badchannel_filename 
    badchannels = np.genfromtxt(bcFname, delimiter=',', dtype='int')
    
    # apply maxfilter to correct for movements and badchannels
    !/neuro/bin/util/maxfilter -f {raw_fname} -o {tsss_fname} -st 10 -movecomp -hp {headpos_logname} -bad {badchannels} -v -force | tee {tsss_logname} 

    # apply maxfilter to make the transformation to 0,0,0
    !/neuro/bin/util/maxfilter -f {tsss_fname} -o {trans_fname} -trans default -force -v | tee {trans_logname}





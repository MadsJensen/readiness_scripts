

def mfFunction(sub_id):
   

    # Paths
    project_path = "/projects/MINDLAB2011_24-MEG-readiness/"
    badchannel_path = project_path + "scripts/Badchannels/"
    
# file names
    raw_fname = "sub_" + str(sub_id) + "_planning_raw.fif"  
    tsss_fname = "sub_" + str(sub_id) + "_tsss_mc.fif"   
    tsss_logname = "sub_" + str(sub_id) + "_tsss_mc.log" 
    trans_fname = "sub_" + str(sub_id) + "_tsss_mc_trans.fif" 
    trans_logname = "sub_" + str(sub_id) + "_tsss_mc_trans.log" 
    headpos_log = "sub_" + str(sub_id) + "_headpos.txt"
    
    # setup the badchannels
    badchannel_filename = 'sub_' + str(sub_id) + '_badchannels.csv'
    bcFname = badchannel_path + badchannel_filename 
    badchannels = np.genfromtxt(bcFname, delimiter=',', dtype='int')

    !/neuro/bin/util/maxfilter -f {raw_fname} -o tsss_fname -st 10 -movecomp -hp headpos_logname -bad badchannels -v -force | tee tsss_logname 

#for i in range(len(rawList)):
 #   !/neuro/bin/util/maxfilter -f {outputTsssList[i]} -o {outputTransList[i]} -trans default -force -v | tee {transLog[i]}





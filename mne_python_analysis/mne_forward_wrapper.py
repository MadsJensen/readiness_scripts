


import os
import logging
logger = logging.getLogger('mne')


def mne_forward_wrapper(sub_id, \
        sessions=["classic", "plan", "interupt"], \
        ico=4, mindist=5,  spacing=5, \
        datapath='/projects/MINDLAB2011_24-MEG-readiness/scratch', \
        MRIpath='/projects/MINDLAB2011_24-MEG-readiness/scratch/mri'):
    """ calls mne_setup_forward_model
    """    
    # Run mne_setup_forward_model
    fname = "fs_sub_%d" % sub_id

    cmd = ("mne_setup_forward_model --subject %s --surf --homog --ico %d " 
            % (fname, ico))
    
    st = os.system(cmd)


    # run mne_do_forward_model
    bem = MRIpath + "/%s/bem/%s-5120-bem-sol-fif" %(fname, fname)
    src = MRIpath + "/%s/bem/%s-5-src.fif" % (fname, fname)
    
    for session in sessions:
        
        meas = datapath + "/sub_%d_%s_tsss_mc.fif" %(sub_id, session)
        fwd = datapath + "/sub_%d_%s_tsss_mc_fwd.fif" %(sub_id, session)


        cmd = ("mne_do_forward_solution \
                --overwrite \
                --subject %s\
                --mindist %d \
                --spacing %d \
                --megonly \
                --bem %s \
                --src %s \
                --meas %s \
                --fwd %s"
                %(fname, mindist, spacing, bem, src, meas, fwd))

        logger.info('Running mne_do_forward_model: %s ' % cmd)
        st = os.system(cmd)
        if st != 0:
            raise RuntimeError('mne_do_forward_model returned non-zero exit status %d' % st)
        logger.info('[done]')



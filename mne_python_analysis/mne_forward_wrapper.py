


import os
import logging
logger = logging.getLogger('mne')

def mne_forward_wrapper(sub_id, session, ico=4):
    """ calls mne_setup_forward_model
    """    
    fname = "sub_%d_%s_tsss_mc.fif"    

    cmd = ("mne_setup_forward_model --subject %s --surf --homog --ico %d " 
            % (fname, ico))
    


    logger.info('Running MaxFilter: %s ' % cmd)
    st = os.system(cmd)
    if st != 0:
        raise RuntimeError('mne_setup_forward_model returned non-zero exit status %d' % st)
    logger.info('[done]')



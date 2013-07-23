# This script is heavily based on the forward model script from cam meg wiki @:
# http://imaging.mrc-cbu.cam.ac.uk/meg/AnalyzingData/MNE_ForwardSolution

# variables

datapath='/media/mje/KINGSTON/MEG_libet/Data'    # root directory for your MEG data
MRIpath='/media/mje/KINGSTON/MEG_libet/Data/mri'    # where your MRI subdirectories are

# The subjects and sessions to be used
subjects=(\
    'sub_1' \
)
sessions=(\
    'plan_tsss_mc' \
    'interupt_tsss_mc'\
)

## fresurfer names:
#fs_subjects=(\
    #'fs_sub_1' \
#)

## setup the filename to be used
nsubjects=${#subjects[*]}
lastsubj=`expr $nsubjects - 1`

## Processing

for m in `seq 0 $lastsubj` 
do
  echo " "
  echo " Computing forward solution for SUBJECT  ${fileList[m]}"
  echo " "

  
  ### setup model 1 layer (MEG only)
  mne_setup_forward_model --overwrite  --subject fs_${subjects[m]} --surf --homog --ico 4


    for j in `seq 0 ${lastsession}`
    do
        fname=${subjects[m]}_${sessions[j]}
        #echo ${fname}
        mne_do_forward_solution \
            --overwrite \
            --subject fs_${subjects[m]} \
            --mindist 5 \
            --spacing 5 \
            --megonly \
            --bem ${MRIpath}/fs_${subjects[m]}/bem/fs_${subjects[m]}-5120-bem-sol.fif \
            --src ${MRIpath}/fs_${subjects[m]}/bem/fs_${subjects[m]}-5-src.fif \
            --meas ${datapath}/${fname}.fif \
            --fwd ${datapath}/${fname}_fwd.fif
    done

done # subjects

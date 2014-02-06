# This script is heavily based on the forward model script from cam meg wiki @:
# http://imaging.mrc-cbu.cam.ac.uk/meg/AnalyzingData/MNE_ForwardSolution

# variables
#datapath='/projects/MINDLAB2011_24-MEG-readiness/scratch' # root directory for your MEG data
#MRIpath='/projects/MINDLAB2011_24-MEG-readiness/scratch/mri'    # where your MRI subdirectories are

datapath='/home/mje/Projects/MEG_libet/BST_test/' # root directory for your MEG data
MRIpath='/home/mje/Projects/MEG_libet/BST_test/' # 

# The subjects and sessions to be used
subjects=(\
    'sub_2' \
)
sessions=(\
    'classic_tsss_mc' \
)

## setup the filename to be used
nsessions=${#sessions[*]}
lastsession=`expr $nsessions - 1`

nsubjects=${#subjects[*]}
lastsubj=`expr $nsubjects - 1`
## Processing

for m in `seq 0 $lastsubj` 
do
  echo " "
  echo " Computing forward solution for SUBJECT:  ${subjects[m]}"
  echo " "

  
  ### setup model 1 layer (MEG only)
  mne_setup_forward_model --overwrite  --subject fs_${subjects[m]} --surf --homog --ico 4

  echo " "
  echo "Compute forward model"
  echo " "

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

SUBJECTS_DIR='/projects/MINDLAB2011_24-MEG-readiness/scratch/mri/'    # root directory for MRI data

for SUBJECT in fs_sub_1 fs_sub_2 # use your list of subject names here
do
        # creates surfaces necessary for BEM head models
        mne_watershed_bem --overwrite --subject $SUBJECT
        ln -s $SUBJECTS_DIR/$SUBJECT/bem/watershed/$SUBJECT'_inner_skull_surface' $SUBJECTS_DIR/$SUBJECT/bem/inner_skull.surf
        ln -s $SUBJECTS_DIR/$SUBJECT/bem/watershed/$SUBJECT'_outer_skull_surface' $SUBJECTS_DIR/$SUBJECT/bem/outer_skull.surf
        ln -s $SUBJECTS_DIR/$SUBJECT/bem/watershed/$SUBJECT'_outer_skin_surface'  $SUBJECTS_DIR/$SUBJECT/bem/outer_skin.surf
        ln -s $SUBJECTS_DIR/$SUBJECT/bem/watershed/$SUBJECT'_brain_surface'       $SUBJECTS_DIR/$SUBJECT/bem/brain_surface.surf
        # creates fiff-files for MNE describing MRI data
        mne_setup_mri --overwrite --subject $SUBJECT
        # create a source space from the cortical surface created in Freesurfer
        mne_setup_source_space --spacing 5 --overwrite --subject $SUBJECT
done

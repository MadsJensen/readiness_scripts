

# write the subject numbers needed after the "in"
for i in 4 5 7 8 11 
do
    fname=$(printf 'fs_sub_%d'  $i) 
    mksubjdirs $SUBJECTS_DIR/$fname
done



# write the subject numbers needed after the "in"
for i in 1 2 3
do
    fname=$(printf 'fs_sub_%d'  $i) 
    mksubjdirs $SUBJECTS_DIR/$fname
done

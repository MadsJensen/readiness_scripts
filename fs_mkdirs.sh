

# write the subject numbers needed after the "in"
for i in 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
do
    fname=$(printf 'fs_sub_%d'  $i) 
    mksubjdirs $SUBJECTS_DIR/$fname
done

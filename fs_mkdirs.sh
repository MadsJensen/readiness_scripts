

# write the subject numbers needed after the "in"
for i in 1 6 3
do
    fname=$(printf 'fs_sub_%d'  $i) 
    mksubjdirs $fname
done

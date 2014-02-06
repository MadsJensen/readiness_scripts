 #!/bin/bash 

for i in 4 7 8 11 
do
    fname=$(printf 'fs_sub_%d'  $i) 
    recon-all -subjid $fname -all -use-gpu -no-isrunning
done

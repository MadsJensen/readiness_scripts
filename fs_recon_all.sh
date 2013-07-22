 #!/bin/bash 

for i in 1 2 3
do
    fname=$(printf 'fs_sub_%d'  $i) 
    recon-all -subjid $fname -all -use-gpu -no-isrunning
done

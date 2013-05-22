


plan_fifs = !find  /projects/MINDLAB2011_24-MEG-readiness/raw/ | grep fif | grep 'plan'
classic_fifs = !find  /projects/MINDLAB2011_24-MEG-readiness/raw/ | grep fif | grep 'classic'
inter_fifs = !find  /projects/MINDLAB2011_24-MEG-readiness/raw/ | grep fif | grep 'nter'


# remove sub 1
del plan_fifs[0]
del inter_fifs[0] # remove extra due to search criteria
del inter_fifs[0]

for i in range(len(plan_fifs)):
    subNumber = i + 2
    ln_name_plan = "sub_%d_plan_raw.fif" % subNumber
    ln_name_classic = "sub_%d_classic_raw.fif" % subNumber
    ln_name_interupt = "sub_%d_interupt_raw.fif" % subNumber
    ! ln -s {plan_fifs[i]} {ln_name_plan}
    ! ln -s {classic_fifs[i]} {ln_name_classic}
    ! ln -s {inter_fifs[i]} {ln_name_interupt}

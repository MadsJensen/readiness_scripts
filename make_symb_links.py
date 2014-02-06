
import os

# change to the dir  with the pythoon functions# change to the dir  with the pythoon functions
os.chdir("/projects/MINDLAB2011_24-MEG-readiness/scripts")



p = open("classic_fifs.txt")
classic_list = [line for line in p.readlines()]

p = open("plan_fifs.txt")
plan_list = [line for line in p.readlines()]

p = open("interrupt_fifs.txt")
interrupt_list = [line for line in p.readlines()]


# change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch')


for i in range(len(classic_list)):
    subNumber = i + 2
    ln_name_plan = "sub_%d_plan-raw.fif" % subNumber
    ln_name_classic = "sub_%d_classic-raw.fif" % subNumber
    ln_name_interrupt = "sub_%d_interrupt-raw.fif" % subNumber
    ! ln -s {plan_list[i][:-1]} {ln_name_plan}
    ! ln -s {classic_list[i][:-1]} {ln_name_classic}
    ! ln -s {interrupt_list[i][:-1]} {ln_name_interrupt}

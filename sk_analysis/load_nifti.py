# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:23:10 2014

@author: mje
"""

import nibabel as nib
import numpy as np

cls = nib.load('Group_analysis_classic.nii')
pln = nib.load('Group_analysis_plan.nii')

cls_data = cls.get_data()
pln_data = pln.get_data()


X = []
for j in range(0,13):
    single_sub_data = cls_data[:,:,:,j]
    if j == 0:
        X = single_sub_data.reshape(-1)
    else:
        X = np.vstack([X, single_sub_data.reshape(-1)])

for j in range(0,13):
    single_sub_data = pln_data[:,:,:,j]
    X = np.vstack([X, single_sub_data.reshape(-1)])

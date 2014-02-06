# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 10:23:10 2014

@author: mje
"""

import nibabel as nib
import numpy as np


import scipy.io as sio
import pylab as pl
import csv

import mne
from sklearn import linear_model
from sklearn.cross_validation import StratifiedKFold, permutation_test_score
from sklearn.cross_validation import  cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.linear_model import RandomizedLogisticRegression
from sklearn.externals import joblib
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import LeaveOneOut, ShuffleSplit
from sklearn import preprocessing
from sklearn import lda

n_jobs = 8

cls = nib.load('Classic_-1500_-500.nii')
pln = nib.load('Plan_-1500_-500.nii')

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


X_scl = preprocessing.scale(foobar)


logReg = linear_model.LogisticRegression()
cv = StratifiedKFold(y, 8)
loo = LeaveOneOut(len(y))
 

cross_score_LR = cross_val_score(logReg, X, y, scoring="accuracy", cv = cv, 
                    n_jobs = 8, verbose = True)
                    
print "Cross val score: ", cross_score_LR.mean() 
print "The different cross_scores: ", cross_score_LR


#score, permutation_score, pvalue = permutation_test_score(logReg, X2, y,

#accuracy_score, cv = cv, n_permutations = 200, 
 #       n_jobs = n_jobs, verbose = True)
#print 'Classification score:', score, 'p-value:', pvalue


#### LDA ####
#lda_clf = lda.LDA()
#
#cross_score_LDA = cross_val_score(lda_clf, X_scl, y, accuracy_score, cv = cv, 
#                    n_jobs = n_jobs, verbose = True)
#                    
#print "Cross val score: ", cross_score_LDA.mean() 
#print "The different cross_scores: ", cross_score_LDA
   

#### Naive bayes ####

from sklearn.naive_bayes import GaussianNB
ngb = GaussianNB()

cross_score_NB = cross_val_score(ngb, X_scl, y, scoring="accuracy", cv = loo, 
                    n_jobs = 8, verbose = True)
                    
print "Cross val score: ", cross_score_NB.mean() 
print "The different cross_scores: ", cross_score_NB

score_NB, permutation_score_NB, pvalue_NB = permutation_test_score(ngb, X_scl, y,
        scoring="accuracy", cv = cv, n_permutations = 2000, 
        n_jobs = n_jobs, verbose = True)
print 'Classification score:', score_NB, 'p-value:', pvalue_NB

#### SVM ####
from sklearn.svm import LinearSVC
svc = LinearSVC()

cross_score_SVM = cross_val_score(svc, X_scl, y, scoring="accuracy", cv = loo, 
                    n_jobs = 8, verbose = True)
                    
print "Cross val score: ", cross_score_SVM.mean() 
print "The different cross_scores: ", cross_score_SVM


score_SVM, permutation_score_SVM, pvalue_SVM = permutation_test_score(svc, X, y,
        scoring="accuracy", cv = cv, n_permutations = 500, 
        n_jobs = 8, verbose = True)
print 'Classification score:', score_SVM, 'p-value:', pvalue_SVM

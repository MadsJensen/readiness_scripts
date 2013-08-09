# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:55:58 2013

@author: mje
"""

import scipy.io as sio
import numpy as np
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
from sklearn.cross_validation import LeaveOneOut
from sklearn import preprocessing

n_jobs = 8


import os
## change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch')

### load data ####
sessions  = ["plan", "classic", "interupt"]
subs = [8]
for sub in subs:
    for session in sessions:
        
        f_load = "sub_%d_%s_tsss_mc_epochs.fif" %(sub, session)
        f_save = "sub_%d_%s" % (sub, session)
        print f_load
        print f_save
        epochs = mne.read_epochs(f_load)
        exec("%s=%s" % (f_save, "epochs"))


#### crop & resample ####
sub_8_classic.crop(tmin=-3, tmax=0)
sub_8_plan.crop(tmin=-3, tmax=0)
sub_8_interupt.crop(tmin=-3, tmax=0)

sub_8_classic.resample(sfreq=500, n_jobs=n_jobs)
sub_8_plan.resample(sfreq=500, n_jobs=n_jobs)
sub_8_interupt.resample(sfreq=500, n_jobs=n_jobs)

#### MVPA ####
#epochs_list = [epochs_plan[k] for k in event_id]
#data_picks = fiff.pick_types(epochs_plan.info, meg='grad', exclude ='bads')
#X = [e.get_data()[:, data_picks, :] for e in epochs_list]


n_times = len(epochs_plan.times)
# Take only the data channels (here the gradiometers)
data_picks = fiff.pick_types(epochs_plan.info, meg='grad', exclude='bads')
# Make arrays X and y such that :
# X is 3d with X.shape[0] is the total number of epochs to classify
# y is filled with integers coding for the class to predict
# We must have X.shape[0] equal to y.shape[0]
X = [e.get_data()[:, data_picks, :] for e in epochs_list]
y = [k * np.ones(len(this_X)) for k, this_X in enumerate(X)]
X = np.concatenate(X)
y = np.concatenate(y)


#### setup X & y ####
data_picks = mne.fiff.pick_types(sub_8_plan.info, meg='grad', exclude='bads')
cond_A = sub_8_classic.get_data()[:, data_picks, :]
cond_B = sub_8_plan.get_data()[:, data_picks, :]
cond_C = sub_8_interupt.get_data()[:, data_picks, :]
n_trials = np.min([len(cond_A), len(cond_B)])

X = np.concatenate([cond_A, cond_B])

for i in range(n_trials):
    foo = cond_A[i, :, :]
    if i == 0:
        X = foo.reshape(-1)
    else:
        X = np.vstack([X, foo.reshape(-1)])

for i in range(n_trials):
    foo = cond_B[i, :, :]
    X = np.vstack([X, foo.reshape(-1)])

for i in range(n_trials):
    foo = cond_C[i, :, :]
    X = np.vstack([X, foo.reshape(-1)])

y = np.concatenate((np.zeros(n_trials), np.ones(n_trials), np.ones(n_trials)*2))
#y = np.concatenate((np.zeros(n_trials), np.ones(n_trials)))
X2 = X*1e12
     

#### find C_param ####

logistic = linear_model.LogisticRegression()
pipe = Pipeline(steps=[('logistic', logistic)])

Cs = np.logspace(-100, 100, 10)
#Parameters of pipelines can be set using ‘__’ separated parameter names:

estimator = GridSearchCV(pipe, dict(logistic__C=Cs))
estimator.fit(X2, y)

C_param = estimator.best_params_['logistic__C']


#### Logistic regression analysis ####

logReg = linear_model.LogisticRegression()
cv = StratifiedKFold(y, 10)
loo = LeaveOneOut(len(y))

cross_score_LR = cross_val_score(logReg, X2, y, accuracy_score, cv = cv, 
                    n_jobs = n_jobs, verbose = True)
                    
print "Cross val score: ", cross_score_LR.mean() 
print "The different cross_scores: ", cross_score_LR
   

score, permutation_score, pvalue = permutation_test_score(logReg, X2, y,
        accuracy_score, cv = cv, n_permutations = 200, 
        n_jobs = n_jobs, verbose = True)
print 'Classification score:', score, 'p-value:', pvalue

#### Naive bayes ####

from sklearn.naive_bayes import GaussianNB
ngb = GaussianNB()


cross_score_NB = cross_val_score(ngb, X_scl, y, accuracy_score, cv = cv, 
                    n_jobs = n_jobs, verbose = True)
                    
print "Cross val score: ", cross_score_NB.mean() 
print "The different cross_scores: ", cross_score_NB

score_NB, permutation_score_NB, pvalue_NB = permutation_test_score(ngb, X_scl, y,
        accuracy_score, cv = cv, n_permutations = 1000, 
        n_jobs = n_jobs, verbose = True)
print 'Classification score:', score, 'p-value:', pvalue

#### SVM ####

from sklearn.svm import SVC
svc = SVC()
cv = StratifiedKFold(y, 10)
loo = LeaveOneOut(len(y))

cross_score_SVM = cross_val_score(svc, X2, y, accuracy_score, cv = loo, 
                    n_jobs = n_jobs, verbose = True)
                    
print "Cross val score: ", cross_score_SVM.mean() 
print "The different cross_scores: ", cross_score_SVM







# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 09:55:58 2013

@author: mje
"""

import scipy.io as sio
import numpy as np
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


n_jobs = 8


### load data ####
sessions  = ["plan", "classic"]
subs = [8]
for sub in subs:
    for session in sessions:
        
        f_load = "sub_%d_%s_tsss_mc_epochs.fif" %(sub, session)
        f_save = "sub_%d_%s" % (sub, session)
        print f_load
        print f_save
        epochs = mne.read_epochs(f_load)
        exec("%s=%s" % (f_save, "epochs"))


#### MVPA ####
epochs_list = [epochs_plan[k] for k in event_id]
data_picks = fiff.pick_types(epochs_plan.info, meg='grad', exclude ='bads')
X = [e.get_data()[:, data_picks, :] for e in epochs_list]


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
cond_A = sub_8_classic.get_data()
cond_B = sub_8_plan.get_data()
n_trials = np.min([len(cond_A), len(cond_B)])

for i in range(n_trials):
    foo = cond_A[i, :, :]
    if i == 0:
        X = foo.reshape(-1)
    else:
        X = np.vstack([X, foo.reshape(-1)])

for i in range(n_trials):
    foo = cond_B[i, :, :]
    X = np.vstack([X, foo.reshape(-1)])

y = np.concatenate((np.zeros(n_trials), np.ones(n_trials)))
X2 = X*1e12
     

#### find C_param ####

logistic = linear_model.LogisticRegression()
pipe = Pipeline(steps=[('logistic', logistic)])

Cs = np.logspace(-100, 100, 20)
#Parameters of pipelines can be set using ‘__’ separated parameter names:

estimator = GridSearchCV(pipe, dict(logistic__C=Cs))
estimator.fit(X2, y)

C_param = estimator.best_params_['logistic__C']


#### Logistic regression analysis ####

logReg = linear_model.LogisticRegression(C = C_param)
cv = StratifiedKFold(y, 10)
loo = LeaveOneOut(len(y))

cross_score_LR = cross_val_score(logReg, X2, y, accuracy_score, cv = loo, 
                    n_jobs = n_jobs, verbose = True)
                    
print "Cross val score: ", cross_score_LR.mean() 
print "The different cross_scores: ", cross_score_LR
   







# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 11:33:53 2013

@author: mje
"""
import nibabel as nib
import numpy as np

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import LeaveOneOut

def makeX():
    img_A = nib.load('condition_classic.nii')
    img_B = nib.load('condition_plan.nii')
    
    data_A = img_A.get_data()
    data_B = img_B.get_data()
        
    n_trials = np.min([data_A.shape[3], data_B.shape[3]])
    
    X = []
    for i in range(n_trials):
        print "working on %d of 30" % (i+1)
        foo = data_A[:,:,:, i]
        idxok = ~np.isnan(foo)
        
        clean_trial = foo[idxok]    
        
        if i == 0:
            X = clean_trial.reshape(-1)
        else:
            X = np.vstack([X, clean_trial.reshape(-1)])
            
    for i in range(n_trials):
        print "working on %d of 30" % (i+1)
        foo = data_B[:,:,:,i]
        clean_trial = foo[idxok]  
        X = np.vstack([X, clean_trial.reshape(-1)])
            
            
    y = np.concatenate((np.zeros(30), np.ones(30)))
    X_scl = preprocessing.scale(X)
    
    return X_scl, X , y, idxok
    
    
#### NGB features parameters ####
def ngb_feature_map(X, y):
        
    ngb = GaussianNB()
    loo = LeaveOneOut(len(y))
    
    scores = np.zeros(len(y))
    feature_weights_cond_A = np.zeros([len(y), X.shape[1]])
    feature_weights_cond_B = np.zeros([len(y), X.shape[1]])
    
    for ii, (train, test) in enumerate(loo):
        ngb.fit(X[train], y[train])
        y_pred = ngb.predict(X[test])
        y_test = y[test]
        scores[ii] = np.sum(y_pred == y_test) / float(len(y_test))
        feature_weights_cond_A[ii]  = ngb.theta_[0]
        feature_weights_cond_B[ii]  = ngb.theta_[1]
        
    return scores, feature_weights_cond_A, feature_weights_cond_B
    
        
            
        
def cvn_features2nii(sub_id, feature_weights_A, feature_weights_B):
    fname_img = "sub_%d_ngb_feature_weights" % sub_id
    img = nib.load('condition_classic.nii')
    data_A = img.get_data()
    
    foo = data_A[:,:,:, 0]
    idxok = ~np.isnan(foo)
    
    fdata = np.empty(foo.shape)
    fdata[idxok] = feature_weights_A.mean(axis=0)
    
    img._data = fdata        
    nib.save(img, fname_img + "cond_A.nii")
    
    fdata = np.empty(foo.shape)
    fdata[idxok] = feature_weights_B.mean(axis=0)
    
    img._data = fdata        
    nib.save(img, fname_img + "cond_B.nii")
    






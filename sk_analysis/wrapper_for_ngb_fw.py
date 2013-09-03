# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:20:25 2013

@author: mje
"""

subs = [2]

for sub in subs:
    print "making X for subject: %d" %sub
    X_scl, X , y, idxok = makeX()
    print "Making classification for subject: %d" %sub
    scores, feature_weights_A, feature_weights_B = ngb_feature_map(X_scl, y)
    print "saving feature weights as nii for subject: %d" % sub
    cvn_features2nii(sub, feature_weights_A, feature_weights_B)
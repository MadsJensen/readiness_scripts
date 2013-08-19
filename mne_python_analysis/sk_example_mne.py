print __doc__
import pylab as pl
import numpy as np
import os

import mne
from mne import fiff

pl.close('all')

n_jobs = 8


## change data files dir
os.chdir('/projects/MINDLAB2011_24-MEG-readiness/scratch')

### SETUP DATA ####
sessions  = ["plan", "classic"]
subs = [2]
for sub in subs:
    for session in sessions:
        
        f_load = "sub_%d_%s_tsss_mc_epochs.fif" %(sub, session)
        f_save = "sub_%d_%s" % (sub, session)
        print f_load
        print f_save
        epochs = mne.read_epochs(f_load)
        exec("%s=%s" % (f_save, "epochs"))

sub_2_classic.resample(sfreq=500, n_jobs=n_jobs)
sub_2_plan.resample(sfreq=500, n_jobs=n_jobs)
#sub_2_interupt.resample(sfreq=500, n_jobs=n_jobs)

cmb_A = sub_2_classic[:, :, 250:-250]
cmb_B = sub_2_plan[:, :, 250:-250]
#cmb_C = sub_2_interupt[:, :, 250:-250]



###############################################################################
# Decoding in sensor space using a linear SVM
n_times = len(epochs.times)
# Take only the data channels (here the gradiometers)
data_picks = mne.fiff.pick_types(sub_2_plan.info, meg='grad', exclude='bads')
# Make arrays X and y such that :
# X is 3d with X.shape[0] is the total number of epochs to classify
# y is filled with integers coding for the class to predict
# We must have X.shape[0] equal to y.shape[0]
#n_trials = np.min([len(cmb_A), len(cmb_B), len(cmb_C)])
n_trials = np.min([len(cmb_A), len(cmb_B)])

for i in range(n_trials):
    foo = cmb_A[i, :, :]
    if i == 0:
        X = foo.reshape(-1)
    else:
        X = np.vstack([X, foo.reshape(-1)])

for i in range(n_trials):
    foo = cmb_B[i, :, :]
    X = np.vstack([X, foo.reshape(-1)])

#for i in range(n_trials):
    #foo = cmb_C[i, :, :]
    #X = np.vstack([X, foo.reshape(-1)])

#y = np.concatenate((np.zeros(n_trials), np.ones(n_trials), np.ones(n_trials)*2))
y = np.concatenate((np.zeros(n_trials), np.ones(n_trials)))
X2 = X*1e13
X_scl = preprocessing.scale(X)

from sklearn.svm import SVC
from sklearn.cross_validation import cross_val_score, ShuffleSplit

clf = SVC(C=1, kernel='linear')
# Define a monte-carlo cross-validation generator (reduce variance):
cv = ShuffleSplit(len(X), 10, test_size=0.2)

scores = np.empty(n_times)
std_scores = np.empty(n_times)

for t in xrange(n_times):
    Xt = X2[:, :, t]
    # Standardize features
    Xt -= Xt.mean(axis=0)
    Xt /= Xt.std(axis=0)
    # Run cross-validation
    # Note : for sklearn the Xt matrix should be 2d (n_samples x n_features)
    scores_t = cross_val_score(clf, Xt, y, cv=cv, n_jobs=1)
    scores[t] = scores_t.mean()
    std_scores[t] = scores_t.std()

times = 1e3 * epochs.times
scores *= 100  # make it percentage
std_scores *= 100
pl.plot(times, scores, label="Classif. score")
pl.axhline(50, color='k', linestyle='--', label="Chance level")
pl.axvline(0, color='r', label='stim onset')
pl.legend()
hyp_limits = (scores - std_scores, scores + std_scores)
pl.fill_between(times, hyp_limits[0], y2=hyp_limits[1], color='b', alpha=0.5)
pl.xlabel('Times (ms)')
pl.ylabel('CV classification score (% correct)')
pl.ylim([30, 100])
pl.title('Sensor space decoding')
pl.show()


#### IMPORTS ####
import numpy as np
import pylab as pl
import mne
from mne import fiff
#### settings ####
baseline = (-3.5, -3.2)
tmax = 0 # the end of the epoch
tmin = -3.5 # 
reject = dict(grad=4000e-13)
        #eog=150e-6)
t(mag=4e-12) 
include = ['BIO001', 'BIO002']

event_id = dict(press=1)

n_jobs = 8 # the number of processor to use

#### load and filter ####


# plan condition
raw_plan = fiff.Raw('sub_1_plan_tsss_mc.fif', preload = True)
raw_plan.filter(None, 48, n_jobs = n_jobs, verbose = True)
#raw_plan.resample(200)

events_plan = mne.find_events(raw_plan)
picks = mne.fiff.pick_types(raw_plan.info, meg='grad', eeg=False, eog=False, stim=False, exclude='bads')

epochs_plan =  mne.Epochs(raw_plan, events_plan, event_id, tmin, tmax, proj=True, picks=picks, baseline=baseline,  preload=False, reject=reject)

# interupt condition
raw_interupt = fiff.Raw('sub_1_interupt_tsss_mc.fif', preload = True)
raw_interupt.filter(None, 48, n_jobs = n_jobs, verbose = True)
#raw_interupt.resample(200)

events_interupt = mne.find_events(raw_interupt)
picks = mne.fiff.pick_types(raw_interupt.info, meg='grad', eeg=False, eog=False, stim=False, exclude='bads')


# loop to select classic trials in the interupt session
events_interupt_classic = []
events_interupt_interupt = []
for i in range(len(events_interupt)):
    if i > 0:
        if events_interupt[i, 2] == 1 and events_interupt[i-1, 2] == 1:
            events_interupt_classic.append(i)
        elif events_interupt[i, 2] == 1 and events_interupt[i-1, 2] == 2:
            events_interupt_interupt.append(i)

epochs_interupt_classic =  mne.Epochs(raw_interupt, events_interupt[events_interupt_classic], event_id, tmin, tmax, proj=True, picks=picks, baseline=baseline,  preload=False, reject=reject)


#### ICA ####

eog_events = mne.preprocessing.find_eog_events(raw_plan, event_id)
picks = mne.fiff.pick_types(raw.info, meg=False, eeg=False, eog=True, stim=False, exclude='bads')

eog_epochs = mne.Epochs(raw_plan, eog_events, event_id, tmin, tmax, proj=False,  picks=picks, exluce ='bads')


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


data_plan = epochs_plan.get_data()
data_interupt_classic = epochs_interupt_classic.get_data()
n_trials = 19

for i in range(n_trials):
    foo = data_plan[i, :, :]
    if i == 0:
        X = foo.reshape(-1)
    else:
        X = np.vstack([X, foo.reshape(-1)])

for i in range(n_trials):
    foo = data_classic[i, :, :]
    X = np.vstack([X, foo.reshape(-1)])

y = np.concatenate((np.zeros(n_trials), np.ones(n_trials)))
X2 = X*1e12
     

#### functions to moving average

def movingaverage(interval, window_size):
    window = numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')


def ma_datastruct(dataMatrix):

    fooMatrix  = np.empty(dataMatrix.shape)
    
    for i in range(dataMatrix.shape[0]):
        for j in range(dataMatrix.shape[1]):
            bar = dataMatrix[i,j,:]
            fooMatrix[i,j]  = movingaverage(bar, 5)

    return fooMatrix

#### RMS for grads ####


def combine_grads(data):
    from mne.layouts.layout import _merge_grad_data
    data_rms = np.empty([data.shape[0], data.shape[1]/2, data.shape[2]])

    for i in range(len(data)):
        data_rms[i,: :] = _merge_grad_data(data[i,:, :])
    return data_rms





cd '/home/mje/Projects/MEG_libet/Scripts/mne_python_analysis/'

from preproc_function import preproc_funcion

cd '/media/mje/KINGSTON/MEG_libet/Data/'

sessions  = ["plan", "classic"]
subs = [2]
for sub in subs:
    for session in sessions:
        preproc_funcion(sub, session)
        
        f_load = "sub_%d_%s_tsss_mc_epochs.fif" %(sub, session)
        f_save = "sub_%d_%s" % (sub, session)
        print f_load
        print f_save

        epochs = mne.read_epochs(f_load)

        exec("%s=%s" % (f_save, "epochs"))







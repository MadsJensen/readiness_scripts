
import pylab as pl
import mne
from mne.fiff import Evoked
from mne.minimum_norm import make_inverse_operator, apply_inverse, \
                             write_inverse_operator
subId = 2
session = "classic"

fname = "sub_%d_%s_tsss_mc" %(subId, session)

data_path = "/projects/MINDLAB2011_24-MEG-readiness/scratch/"
fname_epochs = data_path + fname + "_epochs.fif"
fname_fwd_meg = data_path + fname + "_fwd.fif"
fname_cov = data_path + fname + "_cov.fif"

epochs = mne.read_epochs(fname_epochs)
evoked = epochs.average()

snr = 3.0
lambda2 = 1.0 / snr ** 2

# Load data
forward_meg = mne.read_forward_solution(fname_fwd_meg, surf_ori=True)
noise_cov = mne.read_cov(fname_cov)

# regularize noise covariance
noise_cov = mne.cov.regularize(noise_cov, evoked.info,
                               mag=0.05, grad=0.05, eeg=0.1, proj=True)

# Restrict forward solution as necessary for MEG
forward_meg = mne.fiff.pick_types_forward(forward_meg, meg=True, eeg=False)

# make an M/EEG, MEG-only, and EEG-only inverse operators
info = evoked.info
inverse_operator_meg = make_inverse_operator(info, forward_meg, noise_cov,
                                              loose=0.2, depth=0.8)

write_inverse_operator('sample_audvis-meg-oct-6-inv.fif',
                       inverse_operator_meg)

# Compute inverse solution
stcs = dict()
stcs['meg'] = apply_inverse(evoked, inverse_operator_meg, lambda2, "dSPM",
                        pick_normal=False)

# Save result in stc files
names = ['meg']
for name in names:
    stcs[name].save('mne_dSPM_inverse-%s' % name)

###############################################################################
# View activation time-series
pl.close('all')
pl.figure(figsize=(8, 6))
for ii in range(len(stcs)):
    name = names[ii]
    stc = stcs[name]
    pl.subplot(len(stcs), 1, ii + 1)
    pl.plot(1e3 * stc.times, stc.data[::150, :].T)
    pl.ylabel('%s\ndSPM value' % str.upper(name))
pl.xlabel('time (ms)')
pl.show()

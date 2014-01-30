function cvn2rtf(sub_id, session)


fname = sprintf('sub_%d_%s_tsss_mc_preproc_ica.fif', sub_id, session);
oname = ['spmeeg_', fname];

spm('defaults', 'eeg');

S = [];
S.dataset = ['../', fname];
S.mode = 'continuous';
S.channels = {'all'};
S.eventpadding = 0;
S.blocksize = 3276800;
S.checkboundary = 1;
S.saveorigheader = 1;
S.outfile = oname;
S.timewin = [];
S.conditionlabels = {session};
S.inputformat = [];
D = spm_eeg_convert(S);

S = [];
S.D = ['spmeeg_', fname];
S.fsample = 1000;
S.timeonset = 0;
S.bc = 0;
S.inputformat = [];
S.pretrig = -3500;
S.posttrig = 500;
S.trialdef.conditionlabel = 'A';
S.trialdef.eventtype = 'STI101_up';
S.trialdef.eventvalue = 1;
S.reviewtrials = 0;
S.save = 0;
S.epochinfo.padding = 0;
D = spm_eeg_epochs(S);

S = [];
S.D = ['espmeeg_', fname];
S.fsample_new = 250;
S.prefix = 'd';
D = spm_eeg_downsample(S);


S = [];
S.D = ['despmeeg_', fname];
S.methods(1).fun = 'peak2peak';
S.methods(1).channels = 'MEGPLANAR';
S.methods(1).settings.threshold = 200e-12;
S.methods(end+1).fun = 'peak2peak';
S.methods(end).channels = 'MEG';
S.methods(end).settings.threshold = 20e-12;
% S.methods(end+1).fun = 'peak2peak';
% S.methods(end).channels = 'EEG';
% S.methods(end).settings.threshold = 100e-6;
D = spm_eeg_artefact(S);

% 
% S = [];
% S.D = ['adespmeeg_', fname];
% S.channels = {'all'};
% S.frequencies = [8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45];
% S.timewin = [-Inf Inf];
% S.phase = 0;
% S.method = 'morlet';
% S.settings.ncycles = 7;
% S.settings.timeres = 0;
% S.settings.subsample = 1;
% S.prefix = '';
% D = spm_eeg_tf(S);
% 
% 
% S = [];
% S.D = ['tf_adespmeeg_', fname];
% S.mode = 'replace';
% S.prefix = 'P';
% D = spm_eeg_combineplanar(S);
% 
% 
% S = [];
% S.D = ['Ptf_adespmeeg_', fname];
% S.robust = false;
% S.circularise = false;
% S.prefix = 'm';
% D = spm_eeg_average(S);
% 
% 
% S = [];
% S.D = ['mPtf_adespmeeg_', fname];
% S.method = 'Rel';
% S.prefix = 'r';
% S.timewin = [-3500 -3200];
% D = spm_eeg_tf_rescale(S);



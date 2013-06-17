function [preproc_data_grad] = preproc_func(subId, session, Channels)



cfg                         = [];
cfg.dataset                 = ...
  sprintf('sub_%d_%s_tsss_mc.fif', subId, session); 
cfg.trialdef.eventtype      = 'STI101';
cfg.trialdef.eventvalue     = 1; % trigger value
cfg.trialdef.prestim        = 3.5; % in seconds
cfg.trialdef.poststim       = .5; % in seconds

cfg = ft_definetrial(cfg);

%cfg.trl([1,3,6,8,18,28,30,34,36,37,41,43,44,47,48,50,57,58,62,65;],:) =[];

cfg.channel                 = Channels;
cfg.bsfilter                = 'yes';
cfg.bsfreq                  = [49 51; 99 101];
cfg.lpfilter                = 'yes'
cfg.lpfreq                  = 128;

data_GRAD = ft_preprocessing(cfg);


% downsample
cfg                         = [];
cfg.resamplefs              = 256;
cfg.demean                  = 'yes';
cfg.baselinewindow          = [-3.5 -3.1];
cfg.detrend                 = 'no'

data_GRAD = ft_resampledata(cfg, data_GRAD);

preproc_data_grad = data_GRAD;



function [artifact_cfg] = auto_artifact_remove(subId, session, Channels, data)
%This function takes 4 inputs:
% subId: the subject id,
% session: the sesion name
% Channels: the channels to be used
% data: the name of the data to rempve artifacts from. 

fname = sprintf('sub_%d_%s_tsss_mc.fif', subId, session); 

cfg                         = [];
cfg.dataset                 = fname;
cfg.trialdef.eventtype      = 'STI101';
cfg.trialdef.eventvalue     = 1; % trigger value
cfg.trialdef.prestim        = 3.5; % in seconds
cfg.trialdef.poststim       = .5; % in seconds

cfg = ft_definetrial(cfg);

% channel selection, cutoff and padding
cfg.artfctdef.zvalue.channel    = Channels;
cfg.artfctdef.zvalue.cutoff     = 20;
cfg.artfctdef.zvalue.trlpadding = 0;
cfg.artfctdef.zvalue.artpadding = 0;
cfg.artfctdef.zvalue.fltpadding = 0;

% algorithmic parameters
cfg.artfctdef.zvalue.cumulative    = 'yes';
cfg.artfctdef.zvalue.medianfilter  = 'yes';
cfg.artfctdef.zvalue.medianfiltord = 9;
cfg.artfctdef.zvalue.absdiff       = 'yes';

% make the process interactive
cfg.artfctdef.zvalue.interactive = 'no';

[cfg, artifact_jump] = ft_artifact_zvalue(cfg);


%
cfg                         = [];
cfg.dataset                 = fname;
cfg.trialdef.eventtype      = 'STI101';
cfg.trialdef.eventvalue     = 1; % trigger value
cfg.trialdef.prestim        = 3.5; % in seconds
cfg.trialdef.poststim       = .5; % in seconds

cfg = ft_definetrial(cfg);


% channel selection, cutoff and padding
cfg.artfctdef.zvalue.channel = Channels;
cfg.artfctdef.zvalue.cutoff      = 4;
cfg.artfctdef.zvalue.trlpadding  = 0;
cfg.artfctdef.zvalue.fltpadding  = 0;
cfg.artfctdef.zvalue.artpadding  = 0.1;

% algorithmic parameters
cfg.artfctdef.zvalue.bpfilter    = 'yes';
cfg.artfctdef.zvalue.bpfreq      = [110 140];
cfg.artfctdef.zvalue.bpfiltord   = 9;
cfg.artfctdef.zvalue.bpfilttype  = 'but';
cfg.artfctdef.zvalue.hilbert     = 'yes';
cfg.artfctdef.zvalue.boxcar      = 0.2;

% make the process interactive
cfg.artfctdef.zvalue.interactive = 'no';

[cfg, artifact_muscle] = ft_artifact_zvalue(cfg);




cfg=[]; 
cfg.artfctdef.reject = 'complete'; % this rejects complete trials, use 'partial' if you want to do partial artifact rejection
cfg.artfctdef.jump.artifact = artifact_jump;
cfg.artfctdef.feedback        = 'no' 
cfg.artfctdef.muscle.artifact = artifact_muscle;
artifact_cfg = cfg;






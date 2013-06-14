

cfg                         = [];
cfg.dataset                 = ''
cfg.header.file             = ''
cfg.trialdef.eventtype      = 'STI101';
cfg.trialdef.eventvalue     = 1; % trigger value
cfg.trialdef.prestim        = 3.5; % in seconds
cfg.trialdef.poststim       = .5; % in seconds

cfg = ft_definetrial(cfg);


cfg.channel            = {'MEGGRAD'};
cfg.bsfilter                = 'yes';
cfg.bsfreq                  = [49 51; 99 100];
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

%


% cfg          = [];
% cfg.method   = 'summary';
% cfg.alim     = 1e-12; 
% cfg.megscale = 1;
% cfg.eogscale = 5e-8; 
% data_GRAD_vis        = ft_rejectvisual(cfg,data_GRAD); 

%
% ICA
cfg        = [];
cfg.runica.pca = 64;
cfg.channel = 'MEGGRAD';
cfg.method = 'runica'; % this is the default and uses the implementation from EEGLAB
data_GRAD_comp = ft_componentanalysis(cfg, data_GRAD);

%
% plot the components for visual inspection
figure
cfg = [];
cfg.component = [1:20];       % specify the component(s) that should be plotted
cfg.layout    = 'neuromag306planar.lay'; % specify the layout file that should be used for plotting
cfg.comment   = 'no';
ft_topoplotIC(cfg, data_GRAD_comp)

cfg = [];
cfg.layout = 'neuromag306planar.lay'; % specify the layout file that should be used for plotting
cfg.viewmode = 'component';
ft_databrowser(cfg, data_GRAD_comp)

%
%%
cfg = [];
cfg.component = [1,4]; % to be removed component(s)%
ses1_GRAD_ica = ft_rejectcomponent(cfg, data_GRAD_comp, data_GRAD)

%

save ses1_GRAD_ica_ft ses1_GRAD_ica

%%

cfg = [];
cfg.keeptrials = 'yes';

data_GRAD_ica_avg = ft_timelockanalysis(cfg, data_ica)


%%

save data_GRAD_ica_avg data_GRAD_ica_avg

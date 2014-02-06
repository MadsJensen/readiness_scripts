

cfg                         = [];
cfg.dataset                 = '../sub_2_classic-tsss-mc-autobad_ver_4.fif';
cfg.trialdef.eventtype      = 'STI101';
cfg.trialdef.eventvalue     = 1; % trigger value
cfg.trialdef.prestim        = 3.5; % in seconds
cfg.trialdef.poststim       = .5; % in seconds

cfg = ft_definetrial(cfg);

% cfg.trl([1,3,6,8,18,28,30,34,36,37,41,43,44,47,48,50,57,58,62,65;],:) =[];
% 
% cfg.channel            = {'MEGGRAD'};
% cfg.bsfilter                = 'yes';
% cfg.bsfreq                  = [49 51; 99 100];
% cfg.lpfilter                = 'yes'
% cfg.lpfreq                  = 128;
% 
data_GRAD = ft_preprocessing(cfg);
% 
% 
% % downsample
% cfg                         = [];
% cfg.resamplefs              = 256;
% cfg.demean                  = 'yes';
% cfg.baselinewindow          = [-3.5 -3.1];
% cfg.detrend                 = 'no'

data = ft_resampledata(cfg, data_GRAD);

%%

cfg = [];

data_avg = ft_timelockanalysis(cfg, data_GRAD)

%%


cfg          = [];

cfg.method   = 'summary';
cfg.alim     = 1e-12; 
cfg.megscale = 1;
cfg.eogscale = 5e-8; 
data_GRAD_vis        = ft_rejectvisual(cfg,data_GRAD); 

%%
% ICA
cfg        = [];
cfg.runica.pca = 64;
cfg.channel = 'MEGGRAD';
cfg.method = 'runica'; % this is the default and uses the implementation from EEGLAB
data_GRAD_comp = ft_componentanalysis(cfg, data_GRAD_vis);

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
cfg.component = [1,4,9]; % to be removed component(s)%
GRAD_ica = ft_rejectcomponent(cfg, data_GRAD_comp, data_GRAD)

%

save sub_1_interupt_ica GRAD_ica

%%

cfg = [];
cfg.keeptrials = 'yes';

data_GRAD_ica_avg = ft_timelockanalysis(cfg, GRAD_ica)


%%

save data_GRAD_ica_avg data_GRAD_ica_avg

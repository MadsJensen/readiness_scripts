% this is statistical analyses that FieldTrip will make

%% Full timewindow for GRADS
clear;


% load the data files
load GA_classic_cmb
load GA_plan_cmb

load neuromag306cmb_neighb.mat
% load neuromag306mag_neighb


cfg = [];
cfg.latency = [-3 .5];
cfg.channel = {'MEGGRAD'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_GRAD_-3_05 stat

%% TOA: -2750 -> -2350 for GRADS
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

load neuromag306cmb_neighb.mat
% load neuromag306mag_neighb.mat


cfg = [];
cfg.latency = [-2.75  -2.35];
cfg.channel = {'MEGGRAD'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_GRAD_-2750_-2350 stat

%% TOA: -500 -> 0 for GRADS
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

load neuromag306cmb_neighb.mat
% load neuromag306mag_neighb.mat


cfg = [];
cfg.latency = [-0.5 0];
cfg.channel = {'MEGGRAD'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_GRAD_-500_0 stat


%% TOA: -2000 -> -500 for GRADS
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

load neuromag306cmb_neighb.mat
% load neuromag306mag_neighb.mat


cfg = [];
cfg.latency = [-2 -0.5];
cfg.channel = {'MEGGRAD'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_GRAD_-2000_-500 stat

%% TOA: 0 -> 500 for GRADS
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

load neuromag306cmb_neighb.mat
% load neuromag306mag_neighb.mat


cfg = [];
cfg.latency = [0 0.5];
cfg.channel = {'MEGGRAD'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_GRAD_0_500 stat

%% Full timewindow for MAGs
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

% load neuromag306cmb_neighb.mat
load neuromag306mag_neighb.mat


cfg = [];
cfg.latency = [-3 .5];
cfg.channel = {'MEGMAG'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_MAG_-3_05 stat

%% TOA: -2750 -> -2350 for MAGs
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

% load neuromag306cmb_neighb.mat
load neuromag306mag_neighb.mat


cfg = [];
cfg.latency = [-2.75  -2.35];
cfg.channel = {'MEGMAG'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_MAG_-2750_-2350 stat

%% TOA: -500 -> 0 for MAGs
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

% neuromag306cmb_neighb
load neuromag306mag_neighb


cfg = [];
cfg.latency = [-0.5 0];
cfg.channel = {'MEGMAG'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_MAG_-500_0 stat


%% TOA: -2000 -> -500 for MAGs
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

% neuromag306cmb_neighb
load neuromag306mag_neighb


cfg = [];
cfg.latency = [-2 -0.5];
cfg.channel = {'MEGMAG'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_MAG_-2000_-500 stat

%% TOA: 0 -> 500 for MAGs
clear;


% load the data files
load GA_classic_cmb;
load GA_plan_cmb;

% neuromag306cmb_neighb
load neuromag306mag_neighb


cfg = [];
cfg.latency = [0 0.5];
cfg.channel = {'MEGMAG'};

cfg.method = 'montecarlo';
cfg.statistic = 'depsamplesT';
cfg.correctm = 'cluster';
cfg.clusteralpha = 0.05;
cfg.clusterstatistic = 'maxsum';
cfg.minnbchan = 2;
cfg.neighbours = neighbours;
cfg.tail = 0;

cfg.clustertail = 0;
cfg.alpha = 0.025;
cfg.numrandomization = 10000;

subj = 12;
design = zeros(2,2*subj);
for i = 1:subj
  design(1,i) = i;
end
for i = 1:subj
  design(1,subj+i) = i;
end
design(2,1:subj)        = 1;
design(2,subj+1:2*subj) = 2;

cfg.design = design;
cfg.uvar  = 1;
cfg.ivar  = 2;

%
[stat] = ft_timelockstatistics(cfg, GA_classic_cmb, GA_plan_cmb)

save stat_MAG_0_500 stat


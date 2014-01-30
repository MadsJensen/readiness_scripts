function [data_combined] = combine_planar(subId, session)
% this function combines the planar gradiometors and then baseline corrects them 
% takes two arguments:
% subId: the subject number
% session: which seesion to use

%% load file with data
eval(sprintf('load sub_%d_%s_ica_removed_grad', subId, session));
%
%% Combine the data
cfg             = [];
cfg.demean      = 'no';
cfg.keeptrials  = 'yes';
%
data_combined = ft_combineplanar(cfg, data_ica_removed)
%
%% demean the data
%cfg             = [];
%cfg.demean      = 'yes';
%cfg.baselinewindow  = [-3.5, -3.1];
%%
%data_demeaned = ft_preprocessing(cfg, data_combined)


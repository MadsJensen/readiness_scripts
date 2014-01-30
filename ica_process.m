function [data_comp] = ica_process(data)
% takes 1 argument:
% data: the data to be analysed


%%
% ICA
cfg        = [];
cfg.runica.pca = 64;
cfg.channel = 'MEG';
cfg.method = 'runica'; % this is the default and uses the implementation from EEGLAB
data_comp = ft_componentanalysis(cfg, data);


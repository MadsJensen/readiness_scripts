function wrapper_ft_pipeline(subid, session)

%% Preprocess data
% all channels
data = preproc_func(subid, session, {'MEG', 'EOG'})
% only gradiometers
data_grad = preproc_func(subid, session, {'MEGGRAD', 'EOG'})
%only magnotometers
data_mag = preproc_func(subid, session, {'MEGMAG', 'EOG'})
%
% save the grads results
eval(sprintf('save sub_%d_%s_preprocess_grad data_grad', subid, session));
% save the mags results
eval(sprintf('save sub_%d_%s_preprocess_mag data_mag', subid, session));
%
%
%% Find artifacts for all channels
[artifact_cfg] = auto_artifact_remove(subid, session, 'MEG', data)
%
% remove artifacts for gradiometers
data_no_arti_grad = ft_rejectartifact(artifact_cfg, data_grad)
% remove artifact for magnotometers
data_no_arti_mag = ft_rejectartifact(artifact_cfg, data_mag)
%
% save the grads results
eval(sprintf('save sub_%d_%s_artifact_removed_grad data_no_arti_grad', subid, session));
% save the mags results
eval(sprintf('save sub_%d_%s_artifact_removed_mag data_no_arti_mag', subid, session));
%
%
% %% find ICA components
% %for grads
% data_no_arti_comp_grads= ica_process(data_no_arti_grad)
% % for mags
% data_no_arti_comp_mags = ica_process(data_no_arti_mag)
% %
% % save the grads results
% eval(sprintf('save sub_%d_%s_ica_comp_grad data_no_arti_comp_grads', subid, session));
% % save the mags results
% eval(sprintf('save sub_%d_%s_ica_comp_mag data_no_arti_comp_mags', subid, session));


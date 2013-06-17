function [ica_cleaned_data] = remove_ica_components(comps_to_remove, ...
  data_comp, data)



cfg = [];
cfg.component = comps_to_remove; % to be removed component(s)%
ica_cleaned_data = ft_rejectcomponent(cfg, data_comp, data);

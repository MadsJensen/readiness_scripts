function ica_remove_comps(subId, session, chan_type, components)

switch chan_type
    case 'grads'
        %load file with data
        eval(sprintf('load sub_%d_%s_artifact_removed_grad', subId, session));
        %load file with components
        eval(sprintf('load sub_%d_%s_ica_comp_grad', subId, session));

        cfg = [];
        cfg.component       = components; % the component(s) to be removed
        cfg.demeani         = 'no';
        data_ica_removed    = ft_rejectcomponent(cfg, data_no_arti_comp_grads, data_no_arti_grad)

        % save the grads results
        eval(sprintf('save sub_%d_%s_ica_removed_grad data_ica_removed', subId, session));
        
    case 'mags'
        %load file with data
        eval(sprintf('load sub_%d_%s_artifact_removed_mag', subId, session));
        %load file with components
        eval(sprintf('load sub_%d_%s_ica_comp_mag', subId, session));


        cfg = [];
        cfg.component       = components; % the component(s) to be removed
        cfg.demean          = 'no';
        data_ica_removed    = ft_rejectcomponent(cfg, data_no_arti_comp_mags, data_no_arti_mag)

        % save the grads results
        eval(sprintf('save sub_%d_%s_ica_removed_mag data_ica_removed', subId, session));
end

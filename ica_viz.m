function ica_viz(subId, session, chan_type)
% takes 3 arguments:
% subId: the subject id number
% session: which session to view
% chan_type: the channels in the data ('grad', 'mag', 'all')

switch chan_type

  case 'grad'

    eval(sprintf('load sub_%d_%s_ica_comp_grad', subId, session));
    
    figure;
    cfg = [];
    cfg.component = [1:20];       % specify the component(s) that should be plotted
    cfg.layout    = 'neuromag306planar.lay'; % specify the layout file that should be used for plotting
    cfg.comment   = 'no';
    ft_topoplotIC(cfg, data_no_arti_comp_grads)
    
    cfg = [];
    cfg.layout = 'neuromag306planar.lay'; % specify the layout file that should be used for plotting
    cfg.viewmode = 'component';
    ft_databrowser(cfg, data_no_arti_comp_grads)
    
    
  case 'mag'

    eval(sprintf('load sub_%d_%s_ica_comp_mag', subId, session));
    
    figure
    cfg = [];
    cfg.component = [1:20];       % specify the component(s) that should be plotted
    cfg.layout    = 'neuromag306mag.lay'; % specify the layout file that should be used for plotting
    cfg.comment   = 'no';
    ft_topoplotIC(cfg, data_no_arti_comp_mags)
    
    cfg = [];
    cfg.layout = 'neuromag306mag.lay'; % specify the layout file that should be used for plotting
    cfg.viewmode = 'component';
    ft_databrowser(cfg, data_no_arti_comp_mags)
    
  case 'all'

    eval(sprintf('load sub_%d_%s_ica_comp_all', subId, session));
    figure
    cfg = [];
    cfg.component = [1:20];       % specify the component(s) that should be plotted
    cfg.layout    = 'neuromag306all.lay'; % specify the layout file that should be used for plotting
    cfg.comment   = 'no';
    ft_topoplotIC(cfg, data__no_arti_comp_all)
    
    cfg = [];
    cfg.layout = 'neuromag306all.lay'; % specify the layout file that should be used for plotting
    cfg.viewmode = 'component';
    ft_databrowser(cfg, data_no_arti_comp_all)
end

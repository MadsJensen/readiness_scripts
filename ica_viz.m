function ica_viz(data, chan_type)
% takes 2 arguments:
% data: the data with the ICA components
% chan_type: the channels in the data ('grad', 'mag', 'all')

switch chan_type
  case 'grad'
    
    figure
    cfg = [];
    cfg.component = [1:20];       % specify the component(s) that should be plotted
    cfg.layout    = 'neuromag306planar.lay'; % specify the layout file that should be used for plotting
    cfg.comment   = 'no';
    ft_topoplotIC(cfg, data)
    
    cfg = [];
    cfg.layout = 'neuromag306planar.lay'; % specify the layout file that should be used for plotting
    cfg.viewmode = 'component';
    ft_databrowser(cfg, data)
    
  case 'mag'
    figure
    cfg = [];
    cfg.component = [1:20];       % specify the component(s) that should be plotted
    cfg.layout    = 'neuromag306mag.lay'; % specify the layout file that should be used for plotting
    cfg.comment   = 'no';
    ft_topoplotIC(cfg, data)
    
    cfg = [];
    cfg.layout = 'neuromag306mag.lay'; % specify the layout file that should be used for plotting
    cfg.viewmode = 'component';
    ft_databrowser(cfg, data)
    
  case 'all'
    figure
    cfg = [];
    cfg.component = [1:20];       % specify the component(s) that should be plotted
    cfg.layout    = 'neuromag306all.lay'; % specify the layout file that should be used for plotting
    cfg.comment   = 'no';
    ft_topoplotIC(cfg, data_noarti_comp)
    
    cfg = [];
    cfg.layout = 'neuromag306all.lay'; % specify the layout file that should be used for plotting
    cfg.viewmode = 'component';
    ft_databrowser(cfg, data_noarti_comp)
end
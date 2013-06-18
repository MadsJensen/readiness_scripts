function [trl, event] = interupt_select(cfg)

% read the header information and the events from the data
hdr   = ft_read_header(cfg.dataset);
event = ft_read_event(cfg.dataset);

% search for "trigger" events
value  = [event(find(strcmp('STI101', {event.type}))).value]';
sample = [event(find(strcmp('STI101', {event.type}))).sample]';

% determine the number of samples before and after the trigger
pretrig  = -round(cfg.trialdef.prestim  * hdr.Fs);
posttrig =  round(cfg.trialdef.poststim * hdr.Fs);

% look for the combination of a trigger "7" followed by a trigger "64" 
% for each trigger except the last one
trl = [];
for j = 1:(length(value)-1)
  trg1 = value(j);
  trg2 = value(j+1);
  if trg1 == 2 && trg2 == 1
    trlbegin = sample(j+1) + pretrig;       
    trlend   = sample(j+1) + posttrig;       
    offset   = pretrig;
    newtrl   = [trlbegin trlend offset];
    trl      = [trl; newtrl];
  end
end

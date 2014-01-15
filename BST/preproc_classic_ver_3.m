% Script generated by Brainstorm v3.1 (12-Dec-2013)
% edited by mje 15-jan-2014

subs = [4, 7, 8, 9, 10, 11, 13, 14, 15, 16];
% subs = [2];

conditions = {'plan'};

for j = 1:length(subs)
    for k = 1:length(conditions)
        
        % Input files
        sFiles = {...
            sprintf('Subject0%d/@rawsub_%d_%s_tsss_mc_autobad/data_0raw_sub_%d_%s_tsss_mc_autobad.mat', ...
            subs(j), subs(j), conditions{k},  subs(j), conditions{k})};
        
        if subs(j) < 10
            SubjectNames = {sprintf('Subject0%d', subs(j))};
        else
            SubjectNames = {sprintf('Subject%d', subs(j))};
        end
        
        RawFiles = {...
            sprintf('/scratch2/MINDLAB2011_24-MEG-readiness/sub_%d_%s_tsss_mc_autobad.fif', subs(j), conditions{k})...
            sprintf('/scratch2/MINDLAB2011_24-MEG-readiness/sub_%d_%s.eve', subs(j), conditions{k})};
        
        % Start a new report
        bst_report('Start', sFiles);
        
        % Process: Create link to raw file
        sFiles = bst_process(...
            'CallProcess', 'process_import_data_raw', ...
            sFiles, [], ...
            'subjectname', SubjectNames{1}, ...
            'datafile', {RawFiles{1}, 'FIF'}, ...
            'channelreplace', 0, ...
            'channelalign', 1);
        
        % Process: Low-pass:95Hz
        sFiles = bst_process(...
            'CallProcess', 'process_bandpass', ...
            sFiles, [], ...
            'highpass', 0, ...
            'lowpass', 95, ...
            'mirror', 1, ...
            'sensortypes', 'MEG, EEG');
        
        % Process: Detect eye blinks
        % for Subject05 use EOG002
        sFiles = bst_process(...
            'CallProcess', 'process_evt_detect_eog', ...
            sFiles, [], ...
            'channelname', 'EOG001', ...
            'timewindow', [0, 100000], ...
            'eventname', 'blink1');
        
        % Process: SSP EOG: blink1
        sFiles = bst_process(...
            'CallProcess', 'process_ssp_eog', ...
            sFiles, [], ...
            'eventname', 'blink1', ...
            'sensortypes', 'MEG, MEG MAG, MEG GRAD');
        
        % Process: Events: Import from file
        sFiles = bst_process(...
            'CallProcess', 'process_evt_import', ...
            sFiles, [], ...
            'evtfile', {RawFiles{2}, 'FIF'});
        
        % Process: Import MEG/EEG: Events
        sFiles = bst_process(...
            'CallProcess', 'process_import_data_event', ...
            sFiles, [], ...
            'subjectname', SubjectNames{1}, ...
            'condition', conditions{k}, ...
            'eventname', 'Event #1', ...
            'timewindow', [], ...
            'epochtime', [-3.5, 0.5], ...
            'createcond', 0, ...
            'ignoreshort', 1, ...
            'usectfcomp', 1, ...
            'usessp', 1, ...
            'freq', [], ...
            'baseline', [-3.5, -3.3]);
        
        % Process: Remove baseline: [-3500ms,-3300ms]
        sFiles = bst_process(...
            'CallProcess', 'process_baseline', ...
            sFiles, [], ...
            'baseline', [-3.5, -3.3], ...
            'sensortypes', 'MEG, EEG', ...
            'overwrite', 1);
        
        % Process: Detect bad channels: Peak-to-peak  MEGGRAD(0-4000) MEGMAG(0-3500)
        sFiles = bst_process(...
            'CallProcess', 'process_detectbad', ...
            sFiles, [], ...
            'timewindow', [-3.5, 0.5], ...
            'meggrad', [0, 4000], ...
            'megmag', [0, 3500], ...
            'eeg', [0, 0], ...
            'eog', [0, 0], ...
            'ecg', [0, 0], ...
            'rejectmode', 1);  % Reject only the bad channels
        
        
        % Process: Compute head model
        sFiles = bst_process(...
            'CallProcess', 'process_headmodel', ...
            sFiles, [], ...
            'sourcespace', 1, ...
            'meg', 4, ...  % OpenMEEG BEM
            'eeg', 3, ...  % OpenMEEG BEM
            'ecog', 2, ...  % OpenMEEG BEM
            'seeg', 2, ...
            'openmeeg', struct(...
            'BemFiles', {{}}, ...
            'BemNames', {{'Scalp', 'Skull', 'Brain'}}, ...
            'BemCond', [1, 0.0125, 1], ...
            'BemSelect', [1, 1, 1], ...
            'isAdjoint', 0, ...
            'isAdaptative', 1, ...
            'isSplit', 0, ...
            'SplitLength', 4000));
        
        % Save and display report
        ReportFile = bst_report('Save', sFiles);
        bst_report('Open', ReportFile);
        
    end
end

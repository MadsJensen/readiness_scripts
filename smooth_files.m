function smooth_files
fileList = dir('t*.img');

for j = 1:length(fileList)
  P = fileList(j).name;
  Q = ['s', fileList(j).name];
  S = [5 5 10];

  fprintf('smoothing: %d of %d\n', j, length(fileList))
  spm_smooth(P,Q,S)
end

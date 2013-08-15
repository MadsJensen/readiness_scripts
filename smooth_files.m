function smooth_files
fileList = rdir('./**/*.img');

for j = 1:length(fileList)
  P = fileList(j).name;
  Q =  [fileList(j).name(1:end-13), 'strial0001.img'];
  S = [5 5 10];

  fprintf('smoothing: %d of %d\n', j, length(fileList))
  spm_smooth(P,Q,S)
end

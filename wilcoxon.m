% clc;
% clear;
close all;


% Load the fitness data from the MAT-files
results_boaM = load('results_BOA.mat');
results_modified_boa = load('results_Mod_BOA.mat');

% Extract the fitness values from the structures
fitness_boa = results_boaM.results_boaM(:, end); % Assuming the fitness values are stored in the last column
fitness_modified_boa = results_modified_boa.results_modified_boa(:, end); % Assuming the fitness values are stored in the last column

% Perform the Wilcoxon signed-rank test
[p_value, h] = signrank(fitness_boa, fitness_modified_boa);

% Display the p-value and hypothesis test result
disp(['P-value: ', num2str(p_value)]);
if h == 1
    disp('Reject the null hypothesis: There is a significant difference between the two algorithms.');
else
    disp('Fail to reject the null hypothesis: There is no significant difference between the two algorithms.');
end

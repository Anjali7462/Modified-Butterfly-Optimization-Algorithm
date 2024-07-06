function [best_solution, best_fitness] = boa(fitness_function, lower_bound, upper_bound, population_size, max_iterations, a, p)
    % Initialize population
    population = rand(population_size, numel(lower_bound)) .* (upper_bound - lower_bound) + lower_bound;
    best_solution = population(1,:);
    best_fitness = fitness_function(best_solution);

    for iteration = 1:max_iterations
        % Update solutions
        for i = 1:population_size
            solution = population(i,:);
            r = rand();

            % Update using Equation (3)
            if r < p
                butterfly_frequency = a * rand();
                f1 = rand();
                f2 = rand();
                f3 = rand();
                updated_solution = solution + f1 * (solution - best_solution) .* exp(-f2 * butterfly_frequency * ((iteration + 1) / max_iterations).^f3);

            % Update using Equation (4)
            else
                f1 = rand();
                f2 = rand();
                f3 = rand();
                random_individual = population(randi(population_size),:);
                updated_solution = solution + f1 * (solution - random_individual) .* exp(-f2 * butterfly_frequency * ((iteration + 1) / max_iterations).^f3);
            end

            % Clip to bounds
            updated_solution = min(upper_bound, max(lower_bound, updated_solution));

            % Evaluate fitness
            fitness = fitness_function(updated_solution);

            % Update best solution
            if fitness > best_fitness
                best_solution = updated_solution;
                best_fitness = fitness;
            end

            population(i,:) = updated_solution;
        end
    end
end

% Example usage
function fitness = fitness_function(solution)
    % Replace with your fitness function here
    fitness = sum(solution.^2);
end

lower_bound = [0, 0];
upper_bound = [10, 10];
population_size = 20;
max_iterations = 60000;
a = 1.2;
p = 0.8;

% Call the boa function with defined lower and upper bounds
[best_solution, best_fitness] = boa(@fitness_function, lower_bound, upper_bound, population_size, max_iterations, a, p);

disp('Best solution:');
disp(best_solution);
disp('Best fitness:');
disp(best_fitness);

% Store the results in an array for Wilcoxon test
results_boaM = [best_solution, best_fitness];

% Save the results to a MAT-file
save('results_BOA.mat', 'results_boaM');


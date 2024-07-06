import numpy as np
import random
#Original BOA
def boa(fitness_function, lower_bound, upper_bound, population_size=10, max_iterations=6000, a=1.2, p=0.8):

    population = np.random.rand(population_size, len(lower_bound)) * (upper_bound - lower_bound) + lower_bound
    best_solution = population[0]
    best_fitness = fitness_function(best_solution)

    for iteration in range(max_iterations):
        # Update solutions
        for i in range(population_size):
            solution = population[i]
            r = random.random()

            # Update using Equation (3)
            if r < p:
                butterfly_frequency = a * np.random.rand()
                f1 = random.random()
                f2 = random.random()
                f3 = random.random()
                updated_solution = solution + f1 * (solution - best_solution) * np.exp(-f2 * butterfly_frequency * np.power((iteration + 1) / max_iterations, f3))

            # Update using Equation (4)
            else:
                f1 = random.random()
                f2 = random.random()
                f3 = random.random()
                updated_solution = solution + f1 * (solution - random.choice(population)) * np.exp(-f2 * butterfly_frequency * np.power((iteration + 1) / max_iterations, f3))

            # Clip to bounds
            updated_solution = np.clip(updated_solution, lower_bound, upper_bound)

            # Evaluate fitness
            fitness = fitness_function(updated_solution)

            # Update best solution
            if fitness > best_fitness:
                best_solution = updated_solution.copy()
                best_fitness = fitness

            population[i] = updated_solution

    return best_solution, best_fitness

#Modified Boa

def boa(fitness_function, lower_bound, upper_bound, population_size=10, max_iterations=60000, a=1.5, p=0.9):

    population = np.random.rand(population_size, len(lower_bound)) * (upper_bound - lower_bound) + lower_bound
    best_solution = population[0]
    best_fitness = fitness_function(best_solution)

    for iteration in range(max_iterations):
        butterfly_frequency = a * np.random.rand()  # Moved here to make it accessible to both branches
        # Update solutions
        for i in range(population_size):
            solution = population[i]
            r = random.random()

            # Update using Equation (3)
            if r < p:
                f1 = random.random()
                f2 = random.random()
                f3 = random.random()
                updated_solution = solution + f1 * (solution - best_solution) * np.exp(-f2 * butterfly_frequency * np.power((iteration + 1) / max_iterations, f3))

            # Update using an alternative exploitation strategy
            else:
                # Introduce a different exploitation strategy, for example, taking the average of the best solution and a randomly selected solution
                updated_solution = (solution + random.choice(population)) / 2

            # Clip to bounds
            updated_solution = np.clip(updated_solution, lower_bound, upper_bound)

            # Evaluate fitness
            fitness = fitness_function(updated_solution)

            # Update best solution
            if fitness > best_fitness:
                best_solution = updated_solution.copy()
                best_fitness = fitness

            population[i] = updated_solution

    return best_solution, best_fitness

#Testing CEC14 Functions
fitness_functions = [F1, F2, F3, F4, F5, F6, F7, F8, F9, F10,
                     F11, F12, F13, F14, F15, F16, F17, F18, F19, F20,
                     F21, F22, F23, F24, F25, F26, F27, F28, F29, F30]

for i, fitness_function in enumerate(fitness_functions, start=1):
    print(f"Running function F{i}")
    lower_bound = np.full(30, -100)
    upper_bound = np.full(30, 100)
    best_solution, best_fitness = boa(fitness_function, lower_bound, upper_bound)
    print(f"Best solution for F{i}: {best_solution}")
    print(f"Best fitness for F{i}: {best_fitness}\n")


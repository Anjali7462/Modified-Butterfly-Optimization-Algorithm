import numpy as np
import random


def boa(fitness_function, lower_bound, upper_bound, population_size=70, max_iterations=10, a=1.5, p=0.82):

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

# Example usage
def fitness_function(solution):
    # Replace with your fitness function here
    return np.sum(solution**2)

lower_bound = np.array([0, 0])
upper_bound = np.array([15, 15])

best_solution, best_fitness = boa(fitness_function, lower_bound, upper_bound)

print("Best solution:", best_solution)
print("Best fitness:", best_fitness)

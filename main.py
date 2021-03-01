from client import get_errors
import random
import json
# import numpy as np
# 0 = -10
# 1 = swings
# 2 = -10
# 3= 0, -4.5
# 4 = 0.0
# 5 = 0.0
# 6 = -10, 10 train,val
# 7 = 0.0
# 8 = 0.0
# 9 = 0.0
# 10 = 0.0

ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'
OVERFIT_VECTOR = [0.0, -1.457990220064754e-12, -2.2898007842769645e-13, 4.620107525277624e-11, -1.7521481289918844e-10,
                  -1.8366976965696096e-15, 8.529440604118815e-16, 2.2942330256117977e-05, -2.0472100298772093e-06,
                  -1.597928341587757e-08, 9.982140340891233e-10]
POPULATION_SIZE = 10
MUTATION_PROBABILITY = 1
GENERATIONS = 15

def new_individual(individual):
    new_vec = []
    for genome in individual:
        if genome != 0:
            new_genome = genome * (1 + random.uniform(-1,1))
        else:
            new_genome = random.uniform(-10,10)
        new_vec.append(new_genome)
    return new_vec

def create_population():
    population = []
    population.append(OVERFIT_VECTOR)
    for i in range(1,POPULATION_SIZE):
        population.append(new_individual(OVERFIT_VECTOR))
    return population

def calc_weights(population):
    weights = []
    for individual in population:
        train_err, valid_err =  get_errors(ID, individual)
        # valid_err = random.uniform(0,100)
        weights.append(valid_err)
    print(population)
    print(weights)
    max_weight = max(weights)
    weights = [max_weight - weight for weight in weights]
    return weights


def selection(population, weights):
    return random.choices(population,weights=weights,k=2)

def crossover(vectora, vectorb):
    crossover_point = random.randint(1, 10)
    newa = vectora[0:crossover_point] + vectorb[crossover_point:]
    newb = vectorb[0:crossover_point] + vectora[crossover_point:]
    return newa, newb

def next_generation(population, weights):
    next_gen = []
    for i in range(POPULATION_SIZE // 2):
        parenta, parentb = selection(population, weights)
        gena, genb = crossover(parenta, parentb)
        next_gen.append(gena)
        next_gen.append(genb)
    return next_gen


def mutation(population, prob):
    for individual in population:
        index = random.randint(0,10)
        individual[index] += individual[index] * (random.randint(-10,10) / 100)
    return population



def find_solution():
    population = create_population()
    gen_file = open("gen_file.txt", "a")
    for i in range(GENERATIONS):
        print(i)
        weights = calc_weights(population)
        # print(weights)
        population = next_generation(population, weights)
        mutation(population, MUTATION_PROBABILITY)
        gen_file.write(f"\n{i}\n")
        json.dump(population,gen_file)

    gen_file.close()

find_solution()
# [390291186291.0382, 242539265028.76385, 214138031745.40417, 206886489618.1717, 190430080178.52347, 332093872541.82733, 172961207744.41193, 213620720044.12302, 412550658550.62537, 242539265028.76385]




# vector = OVERFIT_VECTOR
# # print(vector, get_errors(ID, vector))
# vector[0] = -10
# vector[2] = -10
# # vector[3] = -4.5
# print(vector, get_errors(ID, vector))

#
# def create_population():
#     pass
#
#
# vectors = create_population()
# for i in range(10):
#     selection(vectors)
#     crossover(vectors)
#     mutation(vectors)

# vector = OVERFIT_VECTOR
# index = 10
# trainerr = []
# valerr = []
# for i in range(-10,11):
#     vector[index] = i
#     train_err, val_err = get_errors(ID, vector)
#     trainerr.append(train_err)
#     valerr.append(val_err)
#
#     print(vector , " : " , train_err, val_err)
# print(min(trainerr), trainerr.index(min(trainerr)) - 10)
# print(min(valerr), valerr.index(min(valerr))  - 10)

# for i in range(11):
#     vector[index] = -0.5 + i/10
#     print(vector , " : " , get_errors(ID,vector))
# from random import choices, randint, randrange, random
# from typing import List, Optional, Callable, Tuple
#
# Genome = List[int]
# Population = List[Genome]
# PopulateFunc = Callable[[], Population]
# FitnessFunc = Callable[[Genome], int]
# SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
# CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
# MutationFunc = Callable[[Genome], Genome]
# PrinterFunc = Callable[[Population, int, FitnessFunc], None]
#
#
# def generate_genome(length: int) -> Genome:
#     return choices([0, 1], k=length)
#
#
# def generate_population(size: int, genome_length: int) -> Population:
#     return [generate_genome(genome_length) for _ in range(size)]
#
#
# def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
#     if len(a) != len(b):
#         raise ValueError("Genomes a and b must be of same length")
#
#     length = len(a)
#     if length < 2:
#         return a, b
#
#     p = randint(1, length - 1)
#     return a[0:p] + b[p:], b[0:p] + a[p:]
#
#
# def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
#     for _ in range(num):
#         index = randrange(len(genome))
#         genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
#     return genome
#
#
# def population_fitness(population: Population, fitness_func: FitnessFunc) -> int:
#     return sum([fitness_func(genome) for genome in population])
#
#
# def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
#     return choices(
#         population=population,
#         weights=[fitness_func(gene) for gene in population],
#         k=2
#     )
#
#
# def sort_population(population: Population, fitness_func: FitnessFunc) -> Population:
#     return sorted(population, key=fitness_func, reverse=True)
#
#
# def genome_to_string(genome: Genome) -> str:
#     return "".join(map(str, genome))
#
#
# def print_stats(population: Population, generation_id: int, fitness_func: FitnessFunc):
#     print("GENERATION %02d" % generation_id)
#     print("=============")
#     print("Population: [%s]" % ", ".join([genome_to_string(gene) for gene in population]))
#     print("Avg. Fitness: %f" % (population_fitness(population, fitness_func) / len(population)))
#     sorted_population = sort_population(population, fitness_func)
#     print(
#         "Best: %s (%f)" % (genome_to_string(sorted_population[0]), fitness_func(sorted_population[0])))
#     print("Worst: %s (%f)" % (genome_to_string(sorted_population[-1]),
#                               fitness_func(sorted_population[-1])))
#     print("")
#
#     return sorted_population[0]
#
#
# def run_evolution(
#         populate_func: PopulateFunc,
#         fitness_func: FitnessFunc,
#         fitness_limit: int,
#         selection_func: SelectionFunc = selection_pair,
#         crossover_func: CrossoverFunc = single_point_crossover,
#         mutation_func: MutationFunc = mutation,
#         generation_limit: int = 100,
#         printer: Optional[PrinterFunc] = None) \
#         -> Tuple[Population, int]:
#     population = populate_func()
#
#     for i in range(generation_limit):
#         population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)
#
#         if printer is not None:
#             printer(population, i, fitness_func)
#
#         if fitness_func(population[0]) >= fitness_limit:
#             break
#
#         next_generation = population[0:2]
#
#         for j in range(int(len(population) / 2) - 1):
#             parents = selection_func(population, fitness_func)
#             offspring_a, offspring_b = crossover_func(parents[0], parents[1])
#             offspring_a = mutation_func(offspring_a)
#             offspring_b = mutation_func(offspring_b)
#             next_generation += [offspring_a, offspring_b]
#
#         population = next_generation
#
#     return population, i
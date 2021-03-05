from client2 import get_errors
import random
import json
import numpy as np
import math

ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'
MAX_DEG = 11
POP_SIZE = 25
MUT_PROB = 0.4
MUT_RANGE = 0.1
VAL_RATIO = 1
TRAIN_RATIO = 1
GENERATIONS = 5
ELITISM = 5  # ALways keep POP_SIZE - ELITISM even
#  Large
# ηc tends to generate children closer to the parents
#  Small
# ηc allows the children to be far from the parents
# 2 to 5 is moderate range

DISTRIBUTION_INDEX = 2
INITIAL_VECTOR = [0,0,0,0,0,0,0,0,0,0,0]


def new_vector(init_vector):
    new_vec = []
    for genome in init_vector:
        if genome != 0:
            new_genome = genome * (1 + random.uniform(-1, 1))
        else:
            new_genome = random.uniform(-10, 10)
        new_vec.append(new_genome)
    return np.array([new_vec])


def create_population(init_vector):
    try:
        with open("output.txt", "r") as file:
            population = json.load(file)
            population = np.array(population)
            return population
    except FileNotFoundError:
        population = np.zeros((POP_SIZE, MAX_DEG), dtype=float)
        population[0] = init_vector
        for i in range(POP_SIZE - 1):
            population[i] = new_vector(init_vector)
        return population


def calc_errors(individual, precalc):
    for item in precalc:
        # comp = individual == item[0]
        if list(individual) == list(item[0]):
            return list(item[1][1:])
    else:
        # return get_errors(ID, individual)
        return [random.uniform(1,1000), random.uniform(1,1000)]

# population = (POP_SIZE * 11) matrix
def calc_weights(population, precalc):
    weights = np.zeros((len(population), 3), dtype=float)
    for i in range(len(population)):
        train_err, validation_err = calc_errors(population[i], precalc)
        weight = 1 / ((train_err + validation_err) + abs(train_err - validation_err))
        weights[i] = weight, train_err, validation_err
    return weights


def mutation(population):
    for individual in population:
        if random.uniform(0, 1) < MUT_PROB:
            for index in range(11):
                individual[index] += individual[index] * random.uniform(-MUT_RANGE, MUT_RANGE)
                individual[index] = max(-10, individual[index])
                individual[index] = min(10, individual[index])
    return population


# p1, p2 are parents each a vector of degree MAX_DEG
def simulated_binary_crossover(p1, p2):
    u = random.random()
    b = None
    if u <= 0.5:
        b = (2 * u) ** (1 / (DISTRIBUTION_INDEX + 1))
    else:
        b = (1 / (2 * (1 - u))) ** (1 / (DISTRIBUTION_INDEX + 1))
    c1 = 0.5 * ((1 + b) * p1 + (1 - b) * p2)
    c2 = 0.5 * ((1 - b) * p1 + (1 + b) * p2)
    return c1, c2


def selection(population, weights):
    length = len(population)
    od_weights = weights[:, :1].flatten()
    sum_weights = sum(od_weights, start=0)
    normal_weights = [weight / sum_weights for weight in od_weights]
    indexes = np.random.choice(a=length, size=2, replace=False, p=normal_weights)
    parents = [population[index] for index in indexes]
    return parents, indexes


def next_generation(population, weights):
    sort_ind = np.argsort(weights, axis=0)[:, :1].flatten()
    sorted_pop = population[sort_ind]
    sorted_weights = weights[sort_ind]

    precalculated = []
    for i in range(ELITISM):
        precalculated.append((sorted_pop[i], sorted_weights[i]))

    # list of [(p1,p2), (c1,c2)] indices p1,p2indices in population and c1,c2 in next_gen
    # element is [(p), (c)] for elitism
    mapping = []

    next_gen = np.zeros((ELITISM, MAX_DEG), dtype=float)
    next_gen[:ELITISM] = sorted_pop[:ELITISM]

    mapping = [[(parent), (child)] for parent, child in zip(sort_ind[:ELITISM], range(ELITISM))]

    for i in range((POP_SIZE - ELITISM) // 2):
        parents, indexes = selection(sorted_pop, weights)

        mapping.append([tuple(indexes), (ELITISM + 2*i, ELITISM + 1 +2*i)])

        p1,p2 = parents
        c1, c2 = simulated_binary_crossover(p1, p2)
        next_gen = np.append(next_gen, np.array([c1]), axis=0)
        next_gen = np.append(next_gen, np.array([c2]), axis=0)

    return precalculated, next_gen, mapping


def genetic_algo():
    gen_file = open("gen_file.txt", "a")
    population = create_population(INITIAL_VECTOR)
    precalc = []

    for i in range(GENERATIONS):

        gen_file.write(f"GENERATION {i + 1}\n\nINITIAL POPULATION\n")
        gen_file.write(str(population))

        weights = calc_weights(population, precalc)

        gen_file.write("\nWEIGHTS\n")
        gen_file.write(str(weights))

        precalc, next_gen, mapping = next_generation(population, weights)

        gen_file.write("\nMAPPING\n")
        gen_file.write(str(mapping))
        gen_file.write("\nAFTER CROSSOVER\n")
        gen_file.write(str(next_gen))

        mutation(next_gen)
        gen_file.write("\nAFTER MUTATION\n")
        gen_file.write(str(next_gen))

        population = next_gen
    gen_file.close()
    with open("output.txt", "w") as file:
        json.dump(population.tolist(),file)

genetic_algo()
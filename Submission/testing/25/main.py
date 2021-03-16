from client import get_errors
import random
import json
import numpy as np

ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'
MAX_DEG = 11
POP_SIZE = 15
MUT_PROB = 0.5
MUT_RANGE = 0.2
VAL_RATIO = 1
TRAIN_RATIO = 1.5
DIFF_RATIO = 0
GENERATIONS = 10
ELITISM = 3
# ALways keep POP_SIZE - ELITISM even
#  Large
# ηc tends to generate children closer to the parents
#  Small
# ηc allows the children to be far from the parents
# 2 to 5 is moderate range

DISTRIBUTION_INDEX = 2
# INITIAL_VECTOR = [0.0, -1.457990220064754e-12, -2.2898007842769645e-13, 4.620107525277624e-11, -1.7521481289918844e-10, -1.8366976965696096e-15, 8.529440604118815e-16, 2.2942330256117977e-05, -2.0472100298772093e-06, -1.597928341587757e-08, 9.982140340891233e-10]

#INITIAL_VECTOR = [-0.08933007119021132, -1.1001744833137864e-13, -5.330174048597786e-14, 9.063416292065155e-12, -2.8011646500420446e-11, -9.883063226946895e-17, 4.42249782519382e-16, 5.882542751830174e-06, -1.224289095588263e-06, -1.9778936908329355e-09, 4.394990712332061e-10]


#INITIAL_VECTOR = [-0.10436880468336364, -1.183406925447938e-13, -4.01347245566295e-14, 9.810773499032495e-12, -3.7142691220788486e-11, -8.108103726656736e-17, 3.270333781478692e-16, 5.120487985759753e-06, -1.1492221700558395e-06, -1.7170943133664252e-09, 4.3048224957241544e-10]


INITIAL_VECTOR = [-0.11905114210956654, -1.2291859884505323e-13, -3.575799947939669e-14, 1.2072062489940233e-11, -3.399427917629721e-11, -9.41727519287464e-17, 3.916896198734941e-16, 6.302957828583797e-06, -1.1185159274790141e-06, -1.4738103752488004e-09, 4.1346546820685834e-10]


assert len(INITIAL_VECTOR) == 11

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
            print("loading old population")
            population = json.load(file)
            population = np.array(population)
            return population
    except FileNotFoundError:
        print("creating new population")
        population = np.zeros((POP_SIZE, MAX_DEG), dtype=float)
        population[0] = init_vector
        #should have been 1,
        for i in range(1, POP_SIZE):
            population[i] = new_vector(init_vector)
        return population


def calc_errors(individual, precalc):
    for item in precalc:
        if list(individual) == list(item[0]):
            return list(item[1][1:])
    else:
        return get_errors(ID, list(individual))
        # return [random.uniform(1,1000), random.uniform(1,1000)]

# population = (POP_SIZE * 11) matrix
def calc_weights(population, precalc):
    weights = np.zeros((len(population), 3), dtype=float)
    for i in range(len(population)):
        train_err, validation_err = calc_errors(population[i], precalc)
        weight = 1 / ((TRAIN_RATIO * train_err + VAL_RATIO * validation_err) + DIFF_RATIO * abs(train_err - validation_err))
        weights[i] = weight, train_err, validation_err
    return weights


def mutation(population):
    for individual in population[ELITISM:]:
        if random.uniform(0, 1) < MUT_PROB:
            for index in range(11):
                individual[index] += individual[index] * random.uniform(-MUT_RANGE, MUT_RANGE)

    for individual in population:
        for index in range(11):
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
    c1 = 0.5 * ((1 - b) * p1 + (1 + b) * p2)
    c2 = 0.5 * ((1 + b) * p1 + (1 - b) * p2)
    return c1, c2


def selection(population, weights):
    length = len(population)
    od_weights = weights[:, :1].flatten()
    sum_weights = sum(od_weights, start=0)
    normal_weights = [weight / sum_weights for weight in od_weights]
    indexes = np.random.choice(a=length, size=2, replace=False, p=normal_weights)
    parents = [population[index] for index in indexes]
    return parents, np.array(indexes)


def next_generation(population, weights):
    sort_ind = np.argsort(weights, axis=0)[:, :1].flatten()
    sort_ind = sort_ind[::-1]
    sorted_pop = population[sort_ind]
    sorted_weights = weights[sort_ind]

    precalculated = [(pop, weight) for pop,weight in zip(sorted_pop[:ELITISM], sorted_weights[:ELITISM])]
    # list of [(p1,p2), (c1,c2)] indices p1,p2indices in population and c1,c2 in next_gen
    # element is [(p), (c)] for elitism
    mapping = []

    next_gen = np.zeros((ELITISM, MAX_DEG), dtype=float)
    next_gen[:ELITISM] = sorted_pop[:ELITISM]

    mapping = [[(parent), (child)] for parent, child in zip(sort_ind[:ELITISM], range(ELITISM))]

    for i in range((POP_SIZE - ELITISM) // 2):
        parents, indexes = selection(sorted_pop, weights)
        indexes = sort_ind[indexes]
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
        print(i)
        gen_file.write(f"\n\n\nGENERATION {i + 1}\n\nINITIAL POPULATION\n")
        gen_file.write(str(population))

        weights = calc_weights(population, precalc)
        print(weights)
        gen_file.write("\n\nWEIGHTS\n")
        gen_file.write(str(weights))

        precalc, next_gen, mapping = next_generation(population, weights)

        gen_file.write("\n\nMAPPING\n")
        gen_file.write(str(mapping))
        gen_file.write("\n\nAFTER CROSSOVER\n")
        gen_file.write(str(next_gen))

        mutation(next_gen)
        gen_file.write("\n\nAFTER MUTATION\n")
        gen_file.write(str(next_gen))

        population = next_gen
    gen_file.close()
    with open("output.txt", "w") as file:
        json.dump(population.tolist(),file)

genetic_algo()

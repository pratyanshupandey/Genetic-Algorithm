file = open("log.txt", "r")
import math
# trrain valid
best_ind_val = ([], [math.inf, math.inf])
best_ind_train = ([], [math.inf, math.inf])
best_ind_overall = ([], [math.inf, math.inf])

def overall(weights):
    # print(weights)
    train_err = weights[0]
    valid_err = weights[1]
    # return train_err
    if train_err == math.inf or valid_err == math.inf:
        weight = 0
    elif (train_err + valid_err) + abs(train_err - valid_err) == 0:
        weight = math.inf
    else:
        weight = 1 / ((train_err + valid_err) + abs(train_err - valid_err))
    # print(train_err, valid_err, weight)
    return weight
def format(line):
    vector, err = line.split(":")
    vector = vector.strip("[] \n").split(", ")
    err = err.strip("[] \n").split(", ")
    vector = [float(num) for num in vector]
    err = [float(num) for num in err]
    return (vector, err)

i = 0
init_pop = []
while True:
    i+=1
    line = file.readline()
    if line == "":
        break
    if line[0] == "[":

        ind = format(line)
        # print("#@#$")
        # print(ind[1], type(ind[1]))
        # if ind[0] == VECTOR:
        #     print(overall(ind[1]))
        # if overall(ind[1]) >4.2e-12:
        #     print(ind[0], overall(ind[1]), ind[1])
        #     init_pop.append(ind)
        if best_ind_val[1][1] > ind[1][1]:
            best_ind_val = ind
        if best_ind_train[1][0] > ind[1][0]:
            best_ind_train = ind
        if overall(best_ind_overall[1]) < overall(ind[1]):
            best_ind_overall = ind

file.close()

print(best_ind_train)
print(best_ind_val)
print(best_ind_overall)

# ([-10.0, -1.457990220064754e-12, -10.0, 4.620107525277624e-11, -1.7521481289918844e-10, -1.8366976965696096e-15, 8.529440604118815e-16, 2.2942330256117977e-05, -2.0472100298772093e-06, -1.597928341587757e-08, 9.982140340891233e-10], [13072745615.275206, 363475493334.69293])
# ([3.1949023879097087, -1.1566445813966808e-12, -1.706303783105885e-13, 7.164510593350617e-11, -2.9798027152778016e-10, -1.4938953170083339e-15, 1.5155307589985295e-15, 3.493791911133584e-05, -2.049689889668182e-06, -9.819094534206726e-09, 7.375886083349607e-10], [1585818192301.4272, 115225209097.53365])
# ([3.527148438220248, -1.1667084630712077e-12, -1.706303783105885e-13, 9.307512270052608e-11, -1.7521481289918844e-10, -2.1685394479697994e-15, 6.35513405133212e-16, 2.2942330256117977e-05, -2.049689889668182e-06, -1.597928341587757e-08, 9.982140340891233e-10], [60135843090.301476, 234428840487.46906])
# print(len(init_pop))
# def sorter(e):
#     return overall(e[1])
# init_pop.sort(key=sorter, reverse=True)
# # for ind in init_pop:
# #     print(ind, overall(ind[1]))
# population = []
# [population.append(x) for x in init_pop if x not in population]
# population = [ind[0] for ind in population]
# print(len(population))
# print(population[:5])


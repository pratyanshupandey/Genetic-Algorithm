from client import get_errors
# import numpy as np
ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'
OVERFIT_VECTOR = [0.0, -1.457990220064754e-12, -2.2898007842769645e-13, 4.620107525277624e-11, -1.7521481289918844e-10, -1.8366976965696096e-15, 8.529440604118815e-16, 2.2942330256117977e-05, -2.0472100298772093e-06, -1.597928341587757e-08, 9.982140340891233e-10]
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
vector = OVERFIT_VECTOR
for i in range(11):
    vector[0] = -10 + i/10
    print(vector , " : " , get_errors(ID,vector))

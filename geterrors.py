from client import get_errors
ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'

# vector = [ 0.00000000e+00, -1.32224490e-12, -2.62445101e-13,  4.00682289e-11,
#  -1.76372543e-10, -1.84826898e-15,  9.51748802e-16,  2.14682832e-05,
#  -2.21274832e-06, -1.49786697e-08,  8.00970477e-10]

# [30685199481870.586, 52628684900433.64]
print(get_errors(ID, vector))

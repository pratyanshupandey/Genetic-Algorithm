import json
from client2 import get_errors
ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'


with open("25.json", "r") as file:
    print("loading old population")
    vectors = json.load(file)

assert len(vectors) == 10
for vector in vectors:
    assert len(vector) == 11
    print(get_errors(ID, vector))

from client2 import get_errors, submit
import json

ID = 'SOql4uavXyMdC9BTYktZDz152sPIhQLm6ucxoy2ujxmqb8o7E1'

with open("Deliverables/allvecs.json", "r") as file:
    print("loading old population")
    vectors = json.load(file)

    for vector in vectors:
        print(vector)
        assert len(vector) == 11
        print(get_errors(ID, vector))
        print(submit(ID, vector))
        inp = input("Continue: ")
        if inp != "y":
            break

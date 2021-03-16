file = open("vectors.txt", "r")
import json

def format(line):
    vector = line.strip("[] ,\n").split(", ")
    vector = [float(num) for num in vector]
    return vector

all_vec = []
while True:
    line = file.readline()
    if line == "":
        break
    if line[0] == "[":
        vector = format(line)
        all_vec.append(vector)

print(len(all_vec))
# file=open('allvecs.json',"w")
# json.dump(all_vec,file)
# file.close()

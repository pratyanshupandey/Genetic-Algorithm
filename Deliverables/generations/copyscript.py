tempelate_file = open("ready_for_gen_file_old23.txt", "r")
vector_file = open("../../NEW2/gen_file_old3.txt", "r")
write_file = open("generations_10.txt", "a")
while True:
    line = tempelate_file.readline()
    if line == "":
        break
    write_file.write(line)

upto = 35986
for i in range(upto):
    line = vector_file.readline()
    write_file.write(line)

vector_file.close()
tempelate_file.close()
write_file.close()
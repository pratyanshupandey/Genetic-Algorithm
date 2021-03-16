file = open("../../NEW2/gen_file_old3.txt", "r")
write_file = open("ready_for_gen_file.txt", "a")
# upto = 4826
# for i in range(upto):
while True:
    line = file.readline()
    if line == "":
        break
    write_file.write(line)

file.close()
write_file.close()
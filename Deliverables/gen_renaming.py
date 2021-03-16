for i in range(1, 11):
    file = f"generations/generations_{i}.txt"
    open_file = open(file, "r")
    write = f"generations_new/generations_{i}.txt"
    write_file = open(write, "a")

    gen = 1
    while True:
        line = open_file.readline()
        if line == "":
            break
        if line[0] == "G":
            line = f"GENERATION {gen}\n"
            gen += 1
        write_file.write(line)
    open_file.close()
    write_file.close()
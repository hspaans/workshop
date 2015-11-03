def grep(what, filename):
    with open(filename) as f:
        for line in f:
            if what in line:
                print(line)



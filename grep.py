def grep(what, filename):
    f = open(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        
        if what in line:
            print(line)
    f.close()


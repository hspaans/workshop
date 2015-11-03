def grep(what, filename):
    f = None
    try:
        f = open(filename)
        while True:
            line = f.readline()
            if len(line) == 0:
                break;
        
            if what in line:
                print(line)
    except IOError:
        print('Could not find file {}'.format(filename))
    finally:
        if f:
            f.close()



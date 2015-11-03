def countdown(n):
    """ generator, count down from n """
    print('Counting down from {:d}'.format(n))
    while n > 0:
        yield n
        n -= 1
    print('{:d} Blast off!'.format(n))
    
    

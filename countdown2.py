class Countdown:
    """ class  to count up or down """
    def __init__(self, start):
        self.start = start

    # Forward Iterator
    def __iter__(self):
        n = self.start
        while n >= 0:
            yield n
            n -= 1

    # Reverse Iterator
    def __reversed__(self):
        n = 0
        while n <= self.start:
            yield n
            n += 1

        

        
            

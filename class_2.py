class Greeter:
    def __init__(self, greet_what = 'world'):
        self.greet_what = greet_what

    def greet(self):
        print('Hello ' + self.greet_what)


try:
    text = input('Enter something > ')
except EOFError:
    print('You gave an EOF!')
except KeyboardInterrupt:
    print('Cancelling eh?')
else:
    print('You entered {}'.format(text))




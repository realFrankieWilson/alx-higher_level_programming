#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    di = number % -10
else:
    di = number % 10

if di > 5:
    print('Last digit of {:d} is {:d} and is greater than 5\
            '.format(number, di))
elif di < 6 and di != 0:
    print('Last digit of {:d} is {:d} and is less than 6 and not 0\
            '.format(number, di))
else:
    print('Last di of {:d} is 0 and is 0'.format(number))

#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)

if num < 0:
    last = num % -10
else:
    last = num % 10

if last > 5:
    print("Last digit of {} is {} and is greater than 5".format(num, last))
elif last == 0:
    print("Last digit of {} is {} and is 0".format(num, last))
elif last < 6 and last != 0:
    print("Last digit of {} is {} and is less than 6 and not 0\
            ".format(num, last))

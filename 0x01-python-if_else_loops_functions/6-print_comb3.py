#!/usr/bin/python3
for i in range(100):
    for n in range(i + 1, 10):
        if i == 8 and n == 9:
            print('89')
        else:
            print('{}{}'.format(i, n), end=', ')

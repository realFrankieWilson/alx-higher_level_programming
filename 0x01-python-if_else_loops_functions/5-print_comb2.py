#!/usr/bin/python3
# A program that prints numbers from 0 to 99
tm = 0
for i in range(100):
    if i == 99:
        print('{}'.format(i), end='\n')
    else:
        print('{:02d}'.format(i), end=', ')

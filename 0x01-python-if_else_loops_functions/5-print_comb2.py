#!/usr/bin/python3
# A program that prints numbers from 0 to 99.
for i in range(10):
    for a in range(10):
        if a <= 9:
            if i == 9 and a == 9:
                print(f'{i}{a}', end="\n")
            else:
                print(f'{i}{a}', end=", ")
        continue

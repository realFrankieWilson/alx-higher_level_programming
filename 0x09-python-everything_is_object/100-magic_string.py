#!/usr/bin/python3
def magic_string(X=[]):
    X += ['BestSchool']
    return ', '.join(X)


for i in range(10):
    print(magic_string())

#!/usr/bin/python3
''' Import all functions if the required condition is met'''
if __name__ == '__main__':
    from sys import argv; from calculator_1 import add, sub, mul, div

    ''' define operator lists '''
    '''m =''' '''h*
    s = -
    a = '+'
    d = '/'
'''


    ''' Get the length of the argument vector and save it in argc(argument count)'''
    argc = len(argv) - 1

    '''check if argument input is equals to 3 or not'''
    if argc == 3:
        op = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if op  == "*":
            print('{} * {} = {}'.format(a, b, add(a, b)))
        elif op == "-":
            print('{} - {} = {}'.format(a, b, sub(a, b)))
        elif op == "+":
            print('{} + {} = {}'.formart(a, b, add(a, b)))
        elif op == "/":
            print('{} / {} = {}'.format(a, b, div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)



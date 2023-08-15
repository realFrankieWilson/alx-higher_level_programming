#!/usr/bin/python3
''' Import all functions if the required condition is met'''
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    ''' Get the length of the argument vector and save\
    it in argc(argument count)'''
    argc = len(argv) - 1

    '''check if argument input is equals to 3 or not'''
    if argc == 3:
        op = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if op == "*":
            print('{:d} * {:d} = {:d}'.format(a, b, add(a, b)))
        elif op == "-":
            print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
        elif op == "+":
            print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
        elif op == "/":
            print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

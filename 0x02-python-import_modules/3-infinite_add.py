#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    lent = len(sys.argv)
    sum = 0
    if lent == 1:
        pass
    else:
        for n in range(1, lent):
            sum += int(sys.argv[n])
    print('{}'.format(sum))

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

a = 0
agv_len = len(sys.argv) - 1
if agv_len == 1:
    print('{} argument:'.format(agv_len))
    print('{}: {}'.format(agv_len, sys.argv[1]))
elif agv_len == 0:
    print('{} arguments.'.format(agv_len))
else:
    print('{} arguments:'.format(agv_len))
    while a < agv_len:
        print('{}: {}'.format(a + 1, sys.argv[a + 1]))
        a += 1

#!/usr/bin/python3
''' The condition prevent direct execution when imported'''
if __name__ == "__main__":
    ''' imports hidden files'''
    import hidden_4

    cont = dir(hidden_4)
    for cont2 in cont:
        if cont2[:2] == '__':
            pass
        else:
            print(cont2)

#!/usr/bin/python3
''' The condition prevent direct execution when imported'''
if __name__ == "__main__":
    ''' imports hidden files'''
    import hidden_4

    file_1 = dir(hidden_4)

    for file_2 in file_1:
        if file_2 == '_':
            pass
        else:
            print(file_2)

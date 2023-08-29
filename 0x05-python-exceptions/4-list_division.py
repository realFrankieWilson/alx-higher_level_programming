#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    lists = []
    tmplst = 0

    for i in range(0, list_length):
        try:
            tmplst = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            tmplst = 0
        except TypeError:
            print("wrong type")
            tmplst = 0
        except IndexError:
            print("out of range")
            tmplst = 0
        finally:
            lists.append(tmplst)
    return lists

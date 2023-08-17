#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        tuple_new = sen_len, None
        return tuple_new
    else:
        tuple_new = sen_len, sentence[0]
        return tuple_new

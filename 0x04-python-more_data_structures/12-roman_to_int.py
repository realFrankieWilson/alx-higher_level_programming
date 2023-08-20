#!/usr/bin/python3
def roman_to_int(roman_string):

    if (not isinstance(roman_string, str) or roman_string is None):
        return 0

    roman_col = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    integ = 0
    rom_len = len(roman_string)

    for i in range(rom_len):
        if roman_col.get(roman_string[i], 0) == 0:
            return 0
        elif ((i != rom_len - 1) and roman_col[roman_string[i]] <
                roman_col[roman_string[i + 1]]):
            integ += roman_col[roman_string[i]] * -1
        else:
            integ += roman_col[roman_string[i]]
    return integ

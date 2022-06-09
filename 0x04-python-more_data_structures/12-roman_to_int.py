#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    # The Roman Numerals DataBase
    rn_db = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Analyse the roman string
    ints = list(map(lambda c: rn_db.get(c, 0), roman_string))
    length = len(ints)
    for a in range(length):
        if a + 1 < length:
            if ints[a] < ints[a + 1]:
                ints[a] = -ints[a]
    return sum(ints)

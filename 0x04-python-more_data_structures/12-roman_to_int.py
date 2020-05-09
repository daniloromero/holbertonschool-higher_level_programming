#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    rom_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 100}
    for k in roman_string:
        if k not in rom_dec:
            return 0
    num = 0
    prev = rom_dec.get(roman_string[0])
    for k in roman_string:
        value = rom_dec.get(k)
        if prev >= value:
            num += value
        elif prev <= value:
            num = num + value - prev * 2
        prev = value
    return num

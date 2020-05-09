#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keylist = list(a_dictionary.keys())
    {a_dictionary.pop(i) for i in keylist if a_dictionary[i] == value}
    return a_dictionary

#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        answer = True
    except ValueError:
        answer = False
    return answer

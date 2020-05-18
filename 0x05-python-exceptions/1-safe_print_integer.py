#!/usr/bin/python3
def safe_print_integer(value):
    try:
        integer = int(value)
        print("{:d}".format(integer))
        return True
    except ValueError:
        return False

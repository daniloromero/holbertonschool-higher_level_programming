#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(*args)
    except Exception as error:
        sys.stderr.write("Execption: " + str(error) + "\n")
        return None

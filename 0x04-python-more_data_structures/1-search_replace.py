#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_x = [replace if i == search else i for i in my_list]
    return list_x

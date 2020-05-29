#!/usr/bin/python3
class LockedClass:
    """ Class locked to first_name, no __dict__ """
    __slots__ = 'first_name'

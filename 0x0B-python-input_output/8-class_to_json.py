#!/usr/bin/python3
"""a python class-to-JSON function"""

def class_to_json(obj):
    """returns the dictionary represntation of simple data structures"""
    return obj.__dict__

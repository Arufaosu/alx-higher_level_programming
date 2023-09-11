#!/usr/bin/python3
"""defines an object attribute lookup function"""

def lookup(obj):
    """returns a list of the object's available attributes"""
    return (dir(obj))

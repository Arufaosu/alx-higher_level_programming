#!/usr/bin/python3
"""defines a class checking function"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class

    Args:
        obj: object to check
        a_class: class to match the type of obj to
    Returns:
        if obj is exactly an instance of a_class True otherwiseits False
    """
    if type(obj) == a_class:
        return True
    return False

#!/usr/bin/python3
"""defines an inherited list class MyList"""


class MyList(list):
    """implements sorted printing for the built-in list class"""

    def print_sorted(self):
        """print the list a in ascending order"""
        print(sorted(self))

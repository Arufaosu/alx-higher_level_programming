#!/usr/bin/python3
"""text file-reading function"""


def read_file(filename=""):
    """prints the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as my_file:
        my_file_contents = my_file.read()

    print(my_file_contents, end="")

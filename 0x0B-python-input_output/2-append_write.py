#!/usr/bin/python3
"""a file-appending function"""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file

    Args:
        filename: name of the file to append to
        text: string to append to the file
    Returns: number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)        

    return len(text)

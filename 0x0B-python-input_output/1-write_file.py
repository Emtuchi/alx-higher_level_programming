#!/usr/bin/python3
"""Writes a string to a text file"""

def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Args:
        filename (str): The name of file to write to.
        text (str): The text to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

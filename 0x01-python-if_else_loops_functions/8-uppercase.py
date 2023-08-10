#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    """Print a string in uppercase."""
    for cat in str:
        if ord(cat) >= 97 and ord(cat) <= 122:
            cat = chr(ord(cat) - 32)
        print("{}".format(cat), end="")
    print("")

#!/usr/bin/python3
# 2-print_alphabet.py

"""Print the alphabet in lowercase, not followed by a new line."""
for letters in range(ord('a'), ord('z') + 1):
    print(chr(letters), end="")

#!/usr/bin/python3
import random

def classify_ls(number):
    digit = abs(number) % 10
    if number < 0:
        digit = -digit

    if digit > 5:
        return "greater than 5"
    elif digit == 0:
        return "0"
    else:
        return "less than 6 and not 0"

number = random.randint(-10000, 10000)
digit = abs(number) % 10
print("Last digit of {} is {} and is {}".format(number, digit, classify_ls(number)))

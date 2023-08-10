#!/usr/bin/python3
import random

number = random.randint(-10, 10)

def classify(number):
    if number > 0:
        return "positive"
    elif number == 0:
        return "zero"
    else:
        return "negative"

print("{} is {}".format(number, classify(number)))


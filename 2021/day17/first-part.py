#!/usr/bin/python3

# Day 16, part 1 of Advent of Code 2021

import sys
import re

regex = "x=(-?\d+)\.\.(-?\d+),.*?(-?\d+)\.\.(-?\d+)"

with open(str(sys.argv[1])) as input_file:
    lowerx, upperx, lowery, uppery = map(int, re.search(regex, input_file.readline()).groups())

print(lowerx, upperx, lowery, uppery)

# Search initial x
x = 0
initx = 0
while not lowerx <= x <= upperx:
    initx += 1
    x = (initx * (initx + 1)) / 2

y = 0
inity = 1000
while not lowery <= y <= uppery:
    inity -= 1
    highest = 0
    y = 0
    i = 0
    while y >= uppery:
        y += inity - i
        if highest < y:
            highest = y
        i += 1




print(initx, inity)
print(highest)

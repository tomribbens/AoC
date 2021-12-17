#!/usr/bin/python3

# Day 16, part 1 of Advent of Code 2021

import sys
import re

regex = "x=(-?\d+)\.\.(-?\d+),.*?(-?\d+)\.\.(-?\d+)"

with open(str(sys.argv[1])) as input_file:
    lowerx, upperx, lowery, uppery = map(int, re.search(regex, input_file.readline()).groups())

print(lowerx, upperx, lowery, uppery)

solutions = []
for i in range(upperx + 1):
    for j in range(lowery, 1000):
        x, y, step = (0, 0, 0)

        while x <= upperx and y >= lowery:
            if x >= lowerx and y <= uppery:
                solutions.append((x, y))
                break
            x += max(0, i - step)
            y += j - step 
            step += 1

print(len(solutions))



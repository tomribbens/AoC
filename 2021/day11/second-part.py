#!/usr/bin/python3

# Day 11, part 1 of Advent of Code 2021

import sys
import numpy as np


with open(str(sys.argv[1])) as input_file:
    octopi = np.array([[int(x) for x in line.strip()] for line in input_file])

day = 0
while True:
    day += 1
    octopi += 1

    flashing = np.where((octopi > 9) & (octopi < 1000))
    while len(flashing[0]) > 0:
        coords = list(zip(flashing[0], flashing[1]))
        for x,y in coords:
            octopi[max(0,x-1):min(octopi.shape[0],x+2), max(0,y-1):min(octopi.shape[1],y+2)] += 1
            octopi[x, y] += 1000
        flashing = np.where((octopi > 9) & (octopi < 1000))


    
    octopi[octopi > 1000] = 0
    if octopi.sum() == 0:
        print(day)
        break

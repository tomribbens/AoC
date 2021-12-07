#!/usr/bin/python3

# Day 7, part 1 of Advent of Code 2021

import sys
import statistics
import math

with open(str(sys.argv[1])) as input_file:
    input_array = list(map(int, input_file.readline().strip().split(","))) 

fuel = 0
horizontal = math.floor(statistics.mean(input_array))

print(horizontal)

for i in input_array:
    change = abs(i - horizontal)
    fuel += change * (change + 1) / 2

print(fuel)

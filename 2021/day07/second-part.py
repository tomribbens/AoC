#!/usr/bin/python3

# Day 7, part 1 of Advent of Code 2021

import sys
import statistics
import math

with open(str(sys.argv[1])) as input_file:
    input_array = list(map(int, input_file.readline().strip().split(","))) 

fuel1 = 0
fuel2 = 0
horizontal = math.floor(statistics.mean(input_array))

print(horizontal)

for i in input_array:
    change1 = abs(i - horizontal)
    change2 = abs(i - (horizontal + 1))
    fuel1 += change1 * (change1 + 1) / 2
    fuel2 += change2 * (change2 + 1) / 2

print(min(fuel1, fuel2))
